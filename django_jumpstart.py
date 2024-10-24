import os
import secrets
import string


__version__ = "0.0.3.1"


def generate_secret_key():
    c = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(secrets.choice(c) for i in range(67))

    if not os.path.exists('.env'):
        with open('.env', 'w') as f_env:
            f_env.write(f'SECRET_KEY="{secret_key}"\n')

        return

    new_env = list()

    with open ('.env', 'r') as f_env:
        for line in f_env:
            if "SECRET_KEY=" in line:
                existing_key = line.split('SECRET_KEY=')[1]

                if existing_key.split():
                    return

                line = f'SECRET_KEY="{secret_key}"\n'

            new_env.append(line)

    with open('.env', 'w') as f_env:
        f_env.writelines(new_env)


if __name__ == '__main__':
    print(f"Django Jumpstart: {__version__}")

    generate_secret_key()
