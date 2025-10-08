key = [
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
    ["C", "F", "H", "U", "E", "B", "Z", "I", "M", "Q", "J", "G", "O", "X", "V", "K", "L", "D", "S", "P", "A", "W", "R", "T", "Y", "N"]
]

Encripted_text = "KDVBMHMCP OEP IEP WVGPVVMEX WCX UE VKUDCHIP IVKEGMQJ SGCCZ QE XA WVVD QE ETCOEX CXUEDS MS IEP NVXUE WCX CG QE PMQU IMEDVXUED CGWCSP UE HVUE WVVD WVGZEXUE VKUDCHIP NEWEX NES WMQB WMED"

list_unencripted = []
for char in Encripted_text:
    if char == " ":   # spatie blijft spatie
        list_unencripted.append(" ")
    elif char in key[1]:   # alleen als het in A-Z zit
        index = key[1].index(char)
        list_unencripted.append(key[0][index])
    else:
        list_unencripted.append(char)  # onbekende tekens blijven zoals ze zijn

text = "".join(list_unencripted)
print(text)
