import click


@click.command()
@click.argument('file_name', type=click.Path())
@click.argument('output_file_name', default='img_bytes.txt', type=click.Path())
def main(file_name, output_file_name):
    # save bytes
    with open(file_name, 'rb') as infile:
        with open(output_file_name, 'w') as outfile:
            outfile.write(str(bytes(infile.read())))


if __name__ == "__main__":
    main()
