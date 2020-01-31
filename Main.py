import bitcoin
import requests

print("Started search...")

def run():
    while True:
        valid_private_key = False
        while not valid_private_key:
            private_key = bitcoin.random_key()
            decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
            valid_private_key = 0 < decoded_private_key < bitcoin.N

        wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
        public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
        r = requests.get("https://blockchain.info/q/getsentbyaddress/"+bitcoin.pubkey_to_address(public_key))
        if int(r.text) > 0:
            print("Bitcoin Address is:", bitcoin.pubkey_to_address(public_key))
            print("Private Key is: ", wif_encoded_private_key)
            print("Balance is: ",r.text)


while True:
    try:
        run()
    except Exception as ex:
        print(ex)
