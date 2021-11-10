Sub Main
    xsh.Screen.Synchronous = True    ' 使窗口显示与当前输出同步  
    xsh.Screen.Send "username" ' 补全用户名，输入字符串，登录跳板机  
    xsh.Screen.Send VbCr   ' 回车
    xsh.Screen.WaitForString "username@172.22.2.253's password: " ' 补全用户名
    xsh.Screen.Send "pwd" ' 补全密码
    xsh.Screen.Send VbCr
    xsh.Screen.WaitForString "(base) username@login01:~$ " ' 补全用户名
    xsh.Screen.Send "ssh gpu01"
    xsh.Screen.Send VbCr
    xsh.Screen.WaitForString "username@gpu01's password: " ' 补全用户名
    xsh.Screen.Send "pwd" ' 补全密码
    xsh.Screen.Send VbCr
End Sub