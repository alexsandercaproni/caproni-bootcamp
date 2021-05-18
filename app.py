from aws_cdk import core


from caproni_infrastructure.data_lake.stack import DataLakeStack
from caproni_infrastructure.glue_catalog.stack import GlueCatalogStack


app = core.App()
data_lake = DataLakeStack(app)
glue_catalog = GlueCatalogStack(app, raw_data_lake_bucket=data_lake.data_lake_raw_bucket, processed_data_lake_bucket=data_lake.data_lake_processed_bucket)
athena = AthenaStack(app)
app.synth()
