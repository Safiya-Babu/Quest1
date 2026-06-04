@echo off
REM Local wrapper to make `adk web` default to port 8002 in this project.
REM If a different port is explicitly provided, it is still honored.

if /I "%1"=="web" (
  shift
  adk.exe web --port 8002 %*
) else (
  adk.exe %*
)
