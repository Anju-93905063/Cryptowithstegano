import sys
from Preprocessing import Preprocessing

class Encryption(Preprocessing):
    def Encrypt(self, EI_S, KEYS):
        E1, E2, E3, E4 = EI_S
        K1, K2, K3, K4 = KEYS

        # First half
        E1 = self.anti_clockwise_CircularShift(E1, 2)
        E1 = self.xor_32bits(E1, K1)
        E3 = self.anti_clockwise_CircularShift(E3, 2)
        E3 = self.xor_32bits(K3, E3)

        E2 = self.xor_32bits(E2, E1)
        E4 = self.xor_32bits(E3, E4)
        E2 = self.clockwise_CircularShift(E2, 2)
        E4 = self.clockwise_CircularShift(E4, 2)
        E2 = self.xor_32bits(K2, E2)
        E4 = self.xor_32bits(K4, E4)

        # Second half
        E1 = self.anti_clockwise_CircularShift(E1, 2)
        E2 = self.anti_clockwise_CircularShift(E2, 2)

        E3 = self.xor_32bits(E1, E3)
        E4 = self.xor_32bits(E4, E2)
        E3 = self.clockwise_CircularShift(E3, 2)
        E4 = self.clockwise_CircularShift(E4, 2)
        CI1 = E3
        CI3 = E4

        E2 = self.xor_32bits(CI3, E2)
        CI4 = E2
        E1 = self.xor_32bits(CI1, E1)
        CI2 = E1

        return (CI1, CI2, CI3, CI4)


def main():
    EI_S = ('E1', 'E2', 'E3', 'E4')  # Example values, replace with actual
    KEYS = ('K1', 'K2', 'K3', 'K4')  # 
    encryption = Encryption()
    cipher_text = encryption.Encrypt(EI_S, KEYS)
    print("Encrypted:", cipher_text)


if __name__ == "__main__":
    print("Start...\n")
    main()
