Import("env")

def burn_bootloader(source, target, env):
    print("Burning bootloader...")
    env.Execute("pio run -t bootloader")

env.AddPreAction("upload", burn_bootloader)