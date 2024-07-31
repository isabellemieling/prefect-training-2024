from prefect import flow


@flow(log_prints=True)
def my_flow(name: str = "World"):
    print(f"Hello {name}!")


if __name__ == "__main__":
    my_flow.from_source(source="https://github.com/isabellemieling/prefect-training-2024", entrypoint="lab104.py:my_flow").deploy(
        name="test-pacc-deployment",
        work_pool_name="testing-workpool",
    )