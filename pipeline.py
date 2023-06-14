import kfp
from kfp import dsl
from kfp.components import func_to_container_op

# @func_to_container_op
# def show_results(decision_tree : float, logistic_regression : float) -> None:
#     # Given the outputs from decision_tree and logistic regression components
#     # the results are shown.
#
#     print(f"Decision tree (accuracy): {decision_tree}")
#     print(f"Logistic regression (accuracy): {logistic_regression}")


@dsl.pipeline(name='First Pipeline', description='Applies Decision Tree and Logistic Regression for classification problem.')
def first_pipeline():

    # Loads the yaml manifest for each component
    download = kfp.components.load_component_from_file('download_data/download_data.yaml')
    # decision_tree = kfp.components.load_component_from_file('decision_tree/decision_tree.yaml')
    # logistic_regression = kfp.components.load_component_from_file('logistic_regression/logistic_regression.yaml')

    # Run download_data task
    download_task = download()

    # Run tasks "decison_tree" and "logistic_regression" given
    # the output generated by "download_task".
    # decision_tree_task = decision_tree(download_task.output)
    # logistic_regression_task = logistic_regression(download_task.output)

    # Given the outputs from "decision_tree" and "logistic_regression"
    # the component "show_results" is called to print the results.
    # show_results(decision_tree_task.output, logistic_regression_task.output)



if __name__ == '__main__':
    kfp.compiler.Compiler().compile(first_pipeline, 'FirstPipeline.yaml')
    # kfp.Client().create_run_from_pipeline_func(basic_pipeline, arguments={})
