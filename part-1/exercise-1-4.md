The initial problem:
```ShellSession
[akseli@aybabtu part-1]$ docker run -it --rm ubuntu sh -c 'while true; do echo "Input website:"; read website; echo "Searching.."; sleep 1; curl http://$website; done'
Input website:
helsinki.fi
Searching..
sh: 1: curl: not found
```

We therefore exit the container and run
```console
[akseli@aybabtu part-1]$ dockerun -it --rm ubuntu
root@b0e9545d0c15:/# apt update
[...]
root@b0e9545d0c15:/# apt -y install curl
[...]
root@b0e9545d0c15:/# sh -c 'while true; do echo "Input website:"; read website; echo "Searching.."; sleep 1; curl http://$website; done'
Input website:
helsinki.fi
Searching..
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.22.1</center>
</body>
</html>
```