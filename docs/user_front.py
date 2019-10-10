import argparse
from handledata import getdata
from decomp import decomp

def main():
    # parser = argparse.ArgumentParser(description="Recommendation via Sparce Matrix Factoring")
    # parser.add_argument('--out-stride', type=int, default=16,
    #                     help='network output stride (default: 8)')

    urm = getdata()
    
    print('urm shape: ',urm.shape)
    
    u, s, vt = decomp(urm)
    
    print(u,s,vt)
    


if __name__ == '__main__':
    main()
    