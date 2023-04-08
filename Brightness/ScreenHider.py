import win32gui
import subprocess
import tkinter as tk
import sys

# add windows you want to dim
# hider_windows = []

def run(cmd):
    return subprocess.run(["powershell", "-Command", cmd], capture_output=True)

def winEnumHandler(hwnd, ctx):
    if(win32gui.IsWindowVisible(hwnd) and len(win32gui.GetWindowText(hwnd)) != 0):
        ctx.append(win32gui.GetWindowText(hwnd))

if __name__ == '__main__':
    open_windows = []
    win32gui.EnumWindows(winEnumHandler, open_windows)
    if(len(set(open_windows) & set(hider_windows)) == 0): sys.exit(0)

    command = f"Write-Host (Get-Ciminstance -Namespace root/WMI -ClassName WmiMonitorBrightness).CurrentBrightness"
    current_brightness = int(run(command).stdout)

    if current_brightness > 50:
        command = f"Write-Host (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,50)"
        run(command)
        print('brightness changed')

