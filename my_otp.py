import pyotp
topt = pyotp.TOTP('HIHKOEWGPXQ3D3BM')
print(topt.now())