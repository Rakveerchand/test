import kfp
from kfp import dsl
from kfp.components import func_to_container_op

@dsl.pipeline(name='First Pipeline', description='Applies Decision Tree and Logistic Regression for classification problem.')
def first_pipeline():

    # Loads the yaml manifest for each component
    
    decision_tree = kfp.components.load_component_from_file('demo/script.yaml')


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(first_pipeline, 'FirstPipeline.yaml')
    # kfp.Client().create_run_from_pipeline_func(basic_pipeline, arguments={})
