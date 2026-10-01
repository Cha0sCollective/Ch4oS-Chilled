param(
    [Parameter(Mandatory = $true)]
    [string]$JavaPath,
    [string]$PackUrl = 'https://raw.githubusercontent.com/Cha0sCollective/Ch4oS-Chilled/main/pack.toml'
)

$ErrorActionPreference = 'Stop'
$bootstrapUrl = 'https://github.com/packwiz/packwiz-installer-bootstrap/releases/download/v0.0.3/packwiz-installer-bootstrap.jar'
$bootstrapHash = 'a8fbb24dc604278e97f4688e82d3d91a318b98efc08d5dbfcbcbcab6443d116c'
$bootstrapPath = Join-Path $PSScriptRoot 'packwiz-installer-bootstrap.jar'

try {
    if (-not (Test-Path -LiteralPath $JavaPath -PathType Leaf)) {
        throw 'Prism did not supply a Java runtime. Select Java 21 in the instance Java settings.'
    }
    # Use the console binary so packwiz progress and errors appear in Prism's log.
    $launchJava = $JavaPath
    if ([IO.Path]::GetFileName($JavaPath) -ieq 'javaw.exe') {
        $consoleJava = Join-Path ([IO.Path]::GetDirectoryName($JavaPath)) 'java.exe'
        if (Test-Path -LiteralPath $consoleJava -PathType Leaf) {
            $launchJava = $consoleJava
        }
    }

    $validBootstrap = (Test-Path -LiteralPath $bootstrapPath -PathType Leaf) -and
        ((Get-FileHash -LiteralPath $bootstrapPath -Algorithm SHA256).Hash -ieq $bootstrapHash)
    if (-not $validBootstrap) {
        Write-Output 'Downloading the official packwiz installer bootstrap...'
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        $temporary = $bootstrapPath + '.download'
        Invoke-WebRequest -UseBasicParsing -Uri $bootstrapUrl -OutFile $temporary
        if ((Get-FileHash -LiteralPath $temporary -Algorithm SHA256).Hash -ine $bootstrapHash) {
            throw 'The packwiz bootstrap download failed its SHA-256 check.'
        }
        Move-Item -LiteralPath $temporary -Destination $bootstrapPath -Force
    }

    Push-Location -LiteralPath $PSScriptRoot
    try {
        Write-Output 'Installing/updating Ch4oS-Chilled through packwiz...'
        & $launchJava -jar $bootstrapPath -g -s client $PackUrl
        if ($LASTEXITCODE -ne 0) {
            throw ('packwiz installation failed with exit code ' + $LASTEXITCODE)
        }
    } finally {
        Pop-Location
    }
} catch {
    Write-Error -ErrorRecord $_ -ErrorAction Continue
    exit 1
}
exit 0
