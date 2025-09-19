

def Person():
    from faker import Faker

    faker = Faker()
    return {
        "name": faker.name(),
        "address": faker.address(),
        "phone": faker.phone_number(),
        "SSN": faker.ssn()
    }


def model(dbt, session):
    dbt.config (
        submission_method = "serverless_cluster"
    )
    import subprocess, sys

    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "faker",  "--quiet", "--disable-pip-version-check"]
        )
    except Exception as e:
        print (f'Package installation failed: {e}')

    personList = [Person() for _ in range(1, 15000)]
    dfPeople = session.createDataFrame(personList)
    return dfPeople