from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import ConsoleSpanExporter



def get_tracer_provider(service_name: str):
    resource = Resource.create({"service.name": service_name})
    tracer_provider = TracerProvider(resource=resource)

    otlp_exporter = OTLPSpanExporter(endpoint="http://tempo:4317", insecure=True)
    span_processor = BatchSpanProcessor(otlp_exporter)
    tracer_provider.add_span_processor(span_processor)

    # Optional: Add a ConsoleSpanExporter for local debugging
    console_processor = BatchSpanProcessor(ConsoleSpanExporter())
    tracer_provider.add_span_processor(console_processor)

    return tracer_provider