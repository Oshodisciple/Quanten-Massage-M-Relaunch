<?php
// Contact form handler: sends one e-mail to the practice, stores nothing on the server.
// Requires PHP mail() on the hosting. If delivery is unreliable, ask the host for SMTP settings.
const TO = 'praxis@quanten-massage-muenchen.de';
const FROM = 'formular@quanten-massage-muenchen.de';   // must be an address on this domain

function clean(string $s, int $max): string {
    $s = trim(str_replace(["\r", "\n"], ' ', $s));
    return mb_substr(strip_tags($s), 0, $max);
}
function back(string $to) { header('Location: ' . $to, true, 303); exit; }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { back('/kontakt/'); }
// spam checks: honeypot, minimum fill time, consent
if (!empty($_POST['website'])) { back('/danke/'); }
$t = (int)($_POST['t'] ?? 0);
if ($t > 0 && (time() - $t) < 4) { back('/danke/'); }
if (empty($_POST['consent'])) { back('/kontakt/'); }

$name  = clean($_POST['name'] ?? '', 80);
$email = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$phone = clean($_POST['phone'] ?? '', 40);
$msg   = trim(strip_tags($_POST['message'] ?? ''));
$msg   = mb_substr($msg, 0, 2000);
if ($name === '' || !$email || $msg === '') { back('/kontakt/'); }

$subject = '=?UTF-8?B?' . base64_encode('Anfrage über die Website von ' . $name) . '?=';
$body = "Name: $name\nE-Mail: $email\nTelefon: " . ($phone ?: '-') . "\n\n$msg\n";
$headers = [
    'From: Website <' . FROM . '>',
    'Reply-To: ' . $name . ' <' . $email . '>',
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
];
$ok = mail(TO, $subject, $body, implode("\r\n", $headers));
back($ok ? '/danke/' : '/kontakt/?fehler=1');
