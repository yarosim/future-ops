param(
  [string]$To,
  [string]$Attachment,
  [string]$Subject = "OpenClaw reports"
)
$ErrorActionPreference = 'Stop'
$envFile = 'C:\Users\YAROS\.openclaw\credentials\email-smtp.env'
if (!(Test-Path $envFile)) { throw "Missing email credentials: $envFile" }
$cfg = @{}
Get-Content $envFile | ForEach-Object {
  if ($_ -match '^([^#=]+)=(.*)$') { $cfg[$matches[1].Trim()] = $matches[2].Trim() }
}
if (!$To) { $To = $cfg.SIMON_EMAIL }
if (!(Test-Path $Attachment)) { throw "Attachment not found: $Attachment" }
$mail = New-Object System.Net.Mail.MailMessage
try {
  $mail.From = New-Object System.Net.Mail.MailAddress($cfg.SMTP_FROM, 'Future - OpenClaw')
  [void]$mail.To.Add($To)
  $mail.Subject = $Subject
  $mail.Body = "Simon,`r`n`r`nAttached is the requested OpenClaw report package.`r`n`r`n- Future (OpenClaw)"
  [void]$mail.Attachments.Add((New-Object System.Net.Mail.Attachment((Resolve-Path $Attachment).Path)))
  $smtp = New-Object System.Net.Mail.SmtpClient($cfg.SMTP_HOST, [int]$cfg.SMTP_PORT)
  $smtp.EnableSsl = $true
  $smtp.Credentials = New-Object System.Net.NetworkCredential($cfg.SMTP_USER, $cfg.SMTP_PASS)
  $smtp.Timeout = 120000
  $smtp.Send($mail)
  Write-Output "SMTP accepted: $To"
} finally {
  if ($mail) { $mail.Dispose() }
  if ($smtp) { $smtp.Dispose() }
}
