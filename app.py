from aws_cdk import core


from infrastructure_caproni_exchange.data_lake.stack import DataLakeStack


app = core.App()
data_lake = DataLakeStack(app)
app.synth()
