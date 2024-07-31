from prefect import flow


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/isabellemieling/prefect-training-2024.git", 
        entrypoint="lab102.py:pipeline"
    ).deploy(
        name="test-pacc-deployment",
        work_pool_name="testing-workpool",
    )