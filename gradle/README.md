# Install latest Gradle on Ubuntu

1. download latest zip at [the gralde releas page](https://gradle.org/releases/).

2. unpzip and sudo cp to say /opt/gradle-6.5.1

3. set path

```
export PATH=$PATH:/opt/gradle-6.5.1/bin
```

and /etc/environment

4. verify

```
gradle -v
```
### next

https://guides.gradle.org/creating-multi-project-builds/
