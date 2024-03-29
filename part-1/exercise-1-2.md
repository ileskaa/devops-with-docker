```console
[akseli@aybabtu part-1]$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
da3b83985f1d12d015bf0b22e7b86674fbf7575a0eef04b01776fede5b0f9d10
4077397cb3b2d6bf2b390ce706d88553e31425ff359a84727e256d89ecac378f
e2060fcac20e975eca469963cd8e786233a3c7f355c291a5310500661913e281

Total reclaimed space: 3.279kB
[akseli@aybabtu part-1]$ docker rmi nginx
Untagged: nginx:latest
Untagged: nginx@sha256:6db391d1c0cfb30588ba0bf72ea999404f2764febf0f1f196acd5867ac7efa7e
Deleted: sha256:92b11f67642b62bbb98e7e49169c346b30e20cd3c1c034d31087e46924b9312e
Deleted: sha256:d9e826dbb4b3c5770fe92638baa8c6614f210d782a5d021a123fe9fa1f92c23d
Deleted: sha256:2a75285e888884bed4d630896c86ecd71739c6e82669e21ad7a050f33c9ac48d
Deleted: sha256:32bfe3f040358ab8f9872a63d4ddefdc68f35d991ca10a812cbac5912ae9f97b
Deleted: sha256:1330486eb62ea7e96f384961b77b0fc85f5d4422e761114ef3a72e7cb89751a4
Deleted: sha256:a375372209a0f2b2c697a52cce46bc41b495bf86184ae83dd5146e20c22078eb
Deleted: sha256:450787ca55caa59d0288de9cf36fc6b77d1b208a77eb837ec3d25b385f99cafb
Deleted: sha256:a483da8ab3e941547542718cacd3258c6c705a63e94183c837c9bc44eb608999
[akseli@aybabtu part-1]$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[akseli@aybabtu part-1]$ docker image ls
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```
