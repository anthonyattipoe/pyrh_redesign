rem @ECHO OFF

rem pushd %~dp0

rem REM Command file for Sphinx documentation

rem if "%SPHINXBUILD%" == "" (
rem 	set SPHINXBUILD=sphinx-build
rem )
rem set SOURCEDIR=.
rem set BUILDDIR=_build

rem if "%1" == "" goto help

rem %SPHINXBUILD% >NUL 2>NUL
rem if errorlevel 9009 (
rem 	echo.
rem 	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
rem 	echo.installed, then set the SPHINXBUILD environment variable to point
rem 	echo.to the full path of the 'sphinx-build' executable. Alternatively you
rem 	echo.may add the Sphinx directory to PATH.
rem 	echo.
rem 	echo.If you don't have Sphinx installed, grab it from
rem 	echo.http://sphinx-doc.org/
rem 	exit /b 1
rem )

rem %SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
rem goto end

rem :help
rem %SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

rem :end
rem popd
