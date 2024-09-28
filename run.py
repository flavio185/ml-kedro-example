# from pathlib import Path
# import mlflow
# from kedro.framework.session import KedroSession
# from kedro.framework.startup import bootstrap_project

# # Initialize the Kedro project
# bootstrap_project(Path.cwd())

# # Set the MLflow tracking URI to your server
# mlflow.set_tracking_uri("http://127.0.0.1:5000")
# mlflow.set_experiment("Kedro Spaceflights test")

# # Enable MLflow autologging
# mlflow.autolog()

# # Define a function to run a specific pipeline
# def run_pipeline(pipeline_name: str, track_pipe: bool = False):
#     with KedroSession.create() as session:
#         if track_pipe:
#             with mlflow.start_run():
#                 mlflow.set_tag("session_id", session.session_id)
#                 mlflow.set_tag("pipeline_name", pipeline_name)
#                 session.run(pipeline_name=pipeline_name)
#         else:
#             session.run(pipeline_name=pipeline_name)

# # Example of running different pipelines
# if __name__ == "__main__":
#     run_pipeline("data_processing")
#     run_pipeline("data_science", track_pipe=True)
