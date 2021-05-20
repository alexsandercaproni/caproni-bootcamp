from aws_cdk import core


from caproni_infrastructure.data_lake.stack import DataLakeStack
from caproni_infrastructure.glue_catalog.stack import GlueCatalogStack
from caproni_infrastructure.athena.stack import AthenaStack
from caproni_infrastructure.kinesis.stack import KinesisStack
from common_stack import CommonStack
from caproni_infrastructure.dms.stack import DmsStack


# Inicia o aplicativo
app = core.App()

data_lake = DataLakeStack(app)
glue_catalog = GlueCatalogStack(
                app,
                raw_data_lake_bucket=data_lake.data_lake_raw_bucket,
                processed_data_lake_bucket=data_lake.data_lake_processed_bucket)

athena = AthenaStack(app)
kineses = KinesisStack(
            app,
            data_lake_raw_bucket=data_lake.data_lake_raw_bucket)

common_stack = CommonStack(app)

dms = DmsStack(
        app,
        common_stack=common_stack,
        data_lake_raw_bucket=data_lake.data_lake_raw_bucket)

# Cria o CloudFormation
app.synth()
