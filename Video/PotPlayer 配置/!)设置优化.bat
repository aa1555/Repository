@ECHO OFF&(PUSHD "%~DP0")&(REG QUERY "HKU\S-1-5-19">NUL 2>&1)||(
powershell -Command "Start-Process '%~sdpnx0' -Verb RunAs"&&EXIT)

:MENU
ECHO.&ECHO  1、设置优化（启用解码器及播放器的基本设置）
ECHO.&ECHO  2、文件关联（默认关联常见的音视频格式文件）

CHOICE /C 12 /N >NUL 2>NUL
IF "%ERRORLEVEL%"=="2" GOTO register
IF "%ERRORLEVEL%"=="1" GOTO Settings

:register
start "" /wait "%~dp0PotPlayerMini64.exe" /RegisterDef
ECHO.&ECHO 完成 &TIMEOUT /t 2 >NUL&CLS&GOTO MENU

:Settings
reg add "HKCU\Software\DAUM\PotPlayerMini64" /f /v "AddMyComPL" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64" /f /v "ServiceValue" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Dialog324" /f /v "TopMost" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "ChatWindowVisible" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "PlayListWindowVisible" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow0" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow1" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow2" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow3" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow4" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow5" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow6" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow7" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow8" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "TopMostWindow9" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "VideoWindowState1" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Positions" /f /v "VideoWindowState2" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "MftDecoder" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "DmoDecoder" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "LastConfigPage" /t REG_DWORD /d "354" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "PlaybackMode" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "ScreenFitMode" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "ScreenFitBySize" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "AudioVolume" /t REG_DWORD /d "55" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "PreviewSeekTime" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "DisplayBookmark" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "PlayScreenSize" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "CloseOnComplete" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "MoveSizeByCenter" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "RememberPosition" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SkinCurrentLeftTime" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "UseMagWindow" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "MinimizeWindowAll" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "EffectPage" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "EffectCastOnly" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SkipCastPreview" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "ChatAttachToMain2" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "BroadcastAttachToMain2" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "PlaylistAttachSize2" /t REG_DWORD /d "286" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SaveCaptionSel" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SaveAudioSel" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "VideoCaptureFolderSelf" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "VideoCaptureTime" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "AudioCaptureFolderSelf" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SavePlayList" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "NoSameFileAddPL" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "VideoTransformUseMode" /t REG_DWORD /d "2" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "IntDXVAUseMode" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "IntDXVAFFmpeg" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "MouseLeftSClick" /t REG_DWORD /d "4" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "MouseLeftDClick" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "PauseOnMin" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "StartScreenSize" /t REG_DWORD /d "3" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "StartScreenSizeUserW" /t REG_DWORD /d "720" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "StartScreenSizeUserH" /t REG_DWORD /d "400" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "StartCenterPos" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "CaptureWithCaption" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "IntH264_0" /t REG_DWORD /d "2" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "IntH265_0" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "BookmarkSaveExternal" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "ThumbnailSameDir" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "ThumbnailCaption" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "DefSizeOnClose" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SO_FolderOpen" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SO_FolderOpenSub" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SO_Playlist" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SO_History" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SO_Fav" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "AttachWindowIndex" /t REG_DWORD /d "2" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SupportH264MVC" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SkinDefaultStart" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SkinSaveSep" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SkinSizePersist" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "SkinPopupMenuStyle" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "InstallEmbeddedFont" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "UseSideWindow" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "RotateScreen" /t REG_DWORD /d "2" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "CaptionMaxRes" /t REG_DWORD /d "1" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "CaptionQueueSize" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "CheckAutoUpdate" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "AutoDownloadFile" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "FileLinkEnqueue" /t REG_DWORD /d "0" >NUL 2>NUL
reg add "HKCU\Software\DAUM\PotPlayerMini64\Settings" /f /v "FileLinkPlay" /t REG_DWORD /d "0" >NUL 2>NUL
ECHO.&ECHO 完成 &TIMEOUT /t 2 >NUL&CLS&GOTO MENU