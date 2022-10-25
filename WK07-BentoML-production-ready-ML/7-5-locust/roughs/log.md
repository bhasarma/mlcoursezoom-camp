When I run  `locust -H http://localhost:3000`, I get the following warning:

```bash
[2022-10-24 08:40:15,481] bsarma-Inspiron-5370/WARNING/locust.main: System open file limit '1024' is below minimum setting '10000'.
It's not high enough for load testing, and the OS didn't allow locust to increase it by itself.
See https://github.com/locustio/locust/wiki/Installation#increasing-maximum-number-of-open-files-limit for more info.
[2022-10-24 08:40:15,482] bsarma-Inspiron-5370/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
[2022-10-24 08:40:15,497] bsarma-Inspiron-5370/INFO/locust.main: Starting Locust 2.12.2
```

Then I go to the link above in warning. This leads me to another [link](https://www.tecmint.com/increase-set-open-file-limits-in-linux/).

I follow the instructions and do the following:

```
cat /proc/sys/fs/file-max
798520

ulimit -Hn
4096

ulimit -Sn
1024

```
