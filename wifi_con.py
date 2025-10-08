import time
from pywifi import PyWiFi, const, Profile

TARGET_SUBSTRING = "LPU"
PASSWORD = "123456789a"
SCAN_TIMEOUT = 8
CONNECT_TIMEOUT = 20

def get_iface():
    wifi = PyWiFi()
    ifaces = wifi.interfaces()
    if not ifaces:
        print("No wireless interface found.")
        exit(1)
    return ifaces[0]

def already_connected(iface, substring):
    iface_status = iface.status()
    if iface_status == const.IFACE_CONNECTED:
        try:
            connected_ssid = iface.network_profiles()[0].ssid
        except Exception:
            connected_ssid = None

        if connected_ssid and substring in connected_ssid and "JioNet" not in connected_ssid:
            print(f"✅ Already connected to {connected_ssid}")
            return True
    return False

def find_ssid(iface, substring):
    iface.scan()
    time.sleep(SCAN_TIMEOUT)
    networks = iface.scan_results()
    best = {}
    for net in networks:
        ss = net.ssid
        if substring in ss and "JioNet" not in ss:
            if ss not in best or net.signal > best[ss].signal:
                best[ss] = net
    if not best:
        return None
    chosen = max(best.values(), key=lambda n: n.signal)
    return chosen.ssid

def connect_to_ssid(iface, ssid, password):
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    for p in iface.network_profiles():
        if p.ssid == ssid:
            iface.remove_network_profile(p)

    tmp_profile = iface.add_network_profile(profile)
    iface.disconnect()
    time.sleep(1)
    iface.connect(tmp_profile)

    start = time.time()
    while time.time() - start < CONNECT_TIMEOUT:
        if iface.status() == const.IFACE_CONNECTED:
            return True
        time.sleep(1)
    return False

def main():
    iface = get_iface()
    
    if already_connected(iface, TARGET_SUBSTRING):
        return

    ssid = find_ssid(iface, TARGET_SUBSTRING)
    if not ssid:
        print(f"No SSID matching '{TARGET_SUBSTRING}' found.")
        return

    print(f"Attempting to connect to: {ssid}")
    ok = connect_to_ssid(iface, ssid, PASSWORD)
    if ok:
        print(f"✅ Connected to {ssid}")
    else:
        print(f"❌ Failed to connect to {ssid} within timeout.")

if __name__ == "__main__":
    main()
