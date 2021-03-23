spin = input()
electric = input()
if spin == '1/2' and electric == '-1/3':
    print('Strange Quark')
elif spin == '1/2' and electric == '2/3':
    print('Charm Quark')
elif spin == '1/2' and electric == '-1':
    print('Electron Lepton')
elif spin == '1/2' and electric == '0':
    print('Neutrino Lepton')
elif spin == '1' and electric == '0':
    print('Photon Boson')
