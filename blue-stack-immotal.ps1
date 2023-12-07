$bluestacksProcessName = "HD-Player"

while ($true) {
    $bluestacksRunning = Get-Process -Name $bluestacksProcessName -ErrorAction SilentlyContinue

    if (!$bluestacksRunning) {
        Write-Host "Bluestack không chạy. Đang khởi động lại..."

        $startInfo = New-Object System.Diagnostics.ProcessStartInfo
        $startInfo.FileName = "C:\Program Files\BlueStacks_nxt\HD-Player.exe"
        $startInfo.Verb = "runas"  # Chạy với quyền admin

        $process = New-Object System.Diagnostics.Process
        $process.StartInfo = $startInfo
        $process.Start() | Out-Null

        Write-Host "Bluestack đã được khởi động lại."
    }
    else {
        Write-Host "Bluestack đang chạy."
    }

    Start-Sleep -Seconds 120
}