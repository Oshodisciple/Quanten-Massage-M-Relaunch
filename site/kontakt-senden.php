<?php
// Contact form handler: sends one e-mail to the practice, stores no form content on the server.
// Requires PHP mail() on the hosting. If delivery is unreliable, ask the host for SMTP settings.
const TO = 'praxis@quanten-massage-muenchen.de';
const FROM = 'formular@quanten-massage-muenchen.de';   // must be an address on this domain
const MAX_PER_WINDOW = 3;                               // rate limit: submissions per IP ...
const WINDOW_SECONDS = 600;                             // ... within 10 minutes

function clean(string $s, int $max): string {
    $s = trim(preg_replace('/[\x00-\x1F\x7F]+/u', ' ', $s));   // no line breaks or control chars: blocks header injection
    return mb_substr(strip_tags($s), 0, $max);
}
function back(string $to) { header('Location: ' . $to, true, 303); exit; }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { back('/kontakt/'); }
if ((int)($_SERVER['CONTENT_LENGTH'] ?? 0) > 20000) { back('/kontakt/?fehler=1'); }

// spam checks: honeypot, minimum fill time (time stamp is set by the page script), consent
if (!empty($_POST['website'])) { back('/danke/'); }
$t = (int)($_POST['t'] ?? 0);
if ($t === 0 || (time() - $t) < 4 || (time() - $t) > 86400) { back('/danke/'); }
if (empty($_POST['consent'])) { back('/kontakt/?fehler=1'); }

// rate limit per IP: only a salted hash and time stamps are kept, in the system temp folder, for 10 minutes
$key = sys_get_temp_dir() . '/qm-rl-' . hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? '') . __FILE__);
$hits = array_filter(array_map('intval', @file($key, FILE_IGNORE_NEW_LINES) ?: []), fn($h) => $h > time() - WINDOW_SECONDS);
if (count($hits) >= MAX_PER_WINDOW) { back('/kontakt/?fehler=2'); }
$hits[] = time();
@file_put_contents($key, implode("\n", $hits), LOCK_EX);

$name  = clean((string)($_POST['name'] ?? ''), 80);
$email = filter_var(trim((string)($_POST['email'] ?? '')), FILTER_VALIDATE_EMAIL);
$phone = clean((string)($_POST['phone'] ?? ''), 40);
$msg   = mb_substr(trim(strip_tags((string)($_POST['message'] ?? ''))), 0, 2000);
if ($name === '' || !$email || strlen($email) > 120 || $msg === '') { back('/kontakt/?fehler=1'); }

$subject = '=?UTF-8?B?' . base64_encode('Anfrage über die Website von ' . $name) . '?=';
$body = "Name: $name\nE-Mail: $email\nTelefon: " . ($phone ?: '-') . "\n\n$msg\n";
$headers = [
    'From: Website <' . FROM . '>',
    'Reply-To: ' . $email,           // validated address only, no free text in headers
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
];
$ok = mail(TO, $subject, $body, implode("\r\n", $headers), '-f' . FROM);
back($ok ? '/danke/' : '/kontakt/?fehler=1');
