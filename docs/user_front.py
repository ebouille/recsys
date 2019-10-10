import argparse


def main():
    parser = argparse.ArgumentParser(description="Recommendation via Sparce Matrix Factoring")
    parser.add_argument('--out-stride', type=int, default=16,
                        help='network output stride (default: 8)')



if __name__ == '__main__':
    main()
    