# MIT License
#
# Copyright (c) 2020 Evgeny Medvedev evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import click

from ethereum2etl.jobs.export_beacon_blocks_job import ExportBeaconBlocksJob

from ethereum2etl.jobs.exporters.ethereum2_item_exporter import Ethereum2ItemExporter
from ethereum2etl.api.ethereum2_teku_api import Ethereum2TekuApi
from blockchainetl_common.logging_utils import logging_basic_config
from blockchainetl_common.thread_local_proxy import ThreadLocalProxy

from ethereum2etl.service.ethereum2_service import Ethereum2Service

logging_basic_config()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-s', '--start-block', default=0, show_default=True, type=int, help='Start block')
@click.option('-e', '--end-block', required=True, type=int, help='End block')
@click.option('-p', '--provider-uri', default='https://medalla.infura.io', show_default=True, type=str,
              help='The URI of the remote Ethereum 2 node')
@click.option('-w', '--max-workers', default=5, show_default=True, type=int, help='The maximum number of workers.')
@click.option('-o', '--output-dir', default=None, type=str, help='The output directory for block data.')
@click.option('-f', '--output-format', default='json', show_default=True, type=click.Choice(['json', 'csv']),
              help='The output format.')
def export_beacon_blocks(start_block, end_block, provider_uri, max_workers, output_dir, output_format):
    """Exports blocks, balance updates, and operations."""

    ethereum2_service = Ethereum2Service(ThreadLocalProxy(lambda: Ethereum2TekuApi(provider_uri)))
    job = ExportBeaconBlocksJob(
        start_block=start_block,
        end_block=end_block,
        ethereum2_service=ethereum2_service,
        max_workers=max_workers,
        item_exporter=Ethereum2ItemExporter(output_dir, output_format=output_format),
    )
    job.run()
