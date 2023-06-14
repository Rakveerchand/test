import kfp
from kfp import dsl


@dsl.pipeline(name='First Pipeline',
              description='Applies Decision Tree and Logistic Regression for classification problem.')
def first_pipeline():
    kfp.components.load_component_from_file('download_data/download_data.yaml')
    kfp.components.load_component_from_file('testing/testing.yaml')


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(first_pipeline, 'FirstPipeline.yaml')
