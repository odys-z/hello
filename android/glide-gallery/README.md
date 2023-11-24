# About

A *Hellow Glide* project.

The source is slightly modified to have sample project depends on gradle dependency.

<span>
<image src="docs/Screenshot_1.png" style="height: 14em"/>
<image src="docs/Screenshot_2.png" style="height: 14em"/>
<image src="docs/Screenshot_3.png" style="height: 14em"/>
</span>

## Credits:

[Glide](https://github.com/bumptech/glide)

[Glide/Sample/Gallery](https://github.com/bumptech/glide/tree/master/samples/gallery)

# Troubleshootings

- Could not start avd

Try start in cli, figure out the error, see [StackOverFlow](https://stackoverflow.com/questions/16717064/emulator-in-android-studio-doesnt-start

```
    $:~/Android/Sdk/tools$ ./emulator -list-avds
    Pixel_2_API_32
    $:~/Android/Sdk/tools$ ./emulator -avd Pixel_2_API_32 -netspeed full -netdelay none
    WARNING | unexpected system image feature string, emulator might not function correctly, please try updating the emulator.
    ProbeKVM: This user doesn't have permissions to use KVM (/dev/kvm).
    The KVM line in /etc/group is: [kvm:x:108:]
```

Fix:

```
    sudo chown ody:ody /dev/kvm
```
