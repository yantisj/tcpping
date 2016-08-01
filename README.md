## Description

Dead simple TCP Ping tool written in Python3. Establishes one connection per
second, times out after one second, and defaults to 10000 connections unless
interrupted with Ctrl-C.

## Usage

```
$ ./tcpping.py
Usage: tcpping.py host [port] [maxCount]
```

## Example
```
./tcpping.py 10.33.1.100 22
Connection timed out!
Connected to 10.33.1.100:22 via TCP: tcp_seq=1 time=39.66 ms
Connected to 10.33.1.100:22 via TCP: tcp_seq=2 time=20.41 ms
Connected to 10.33.1.100:22 via TCP: tcp_seq=3 time=85.18 ms
^C
TCP Ping Results: Connections (Total/Pass/Fail): [4/3/1] (Failed: 25%)
```

## Contributors
* Jonathan Yantis ([yantisj](https://github.com/yantisj))

## License
tcpping is licensed under the GNU AGPLv3 License.
