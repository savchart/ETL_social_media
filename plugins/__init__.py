from airflow.plugins_manager import AirflowPlugin

import operators


class TelegramPlugin(AirflowPlugin):
    name = "telegram_plugin"
    operators = [
        operators.TelegramOperator
    ]


class DiscordPlugin(AirflowPlugin):
    name = "discord_plugin"
    operators = [
        operators.DiscordOperator
    ]


class DataAnalysisPlugin(AirflowPlugin):
    name = "data_analysis_plugin"
    operators = [
        operators.DataAnalysisOperator
    ]


class DataAggregationPlugin(AirflowPlugin):
    name = "data_aggregation_plugin"
    operators = [
        operators.DataAggregationOperator
    ]


class DataVisualizationPlugin(AirflowPlugin):
    name = "data_visualization_plugin"
    operators = [
        operators.DataVisualizationOperator
    ]


class PDFReportPlugin(AirflowPlugin):
    name = "pdf_report_plugin"
    operators = [
        operators.PDFReportOperator
    ]
