# StreamSim

**StreamSim** is a useful tool which is able to encode raw
video material with different settings and stream the encoded results via
pre-defined network configurations in order to insert packet loss resp.
delay/jitter. The transmitted videos are decoded back and can be used to compare
with the original video. It is also possible to insert the loss behaviour
offline, without streaming the content over a physical network.

StreamSim is licensed under GNU GPLv3 (see `License.md`) and can be freely used
and modified.

## How does it work?
The toolchain is separated into five dedicated steps, which can be executed
separately: video encoding, streaming, loss insertion, payload extraction and
decoding. Each step stores its results in a separate folder. It is thus possible
to guard all time the complete chain's process. Futher more each step is
individually configureable and delivers additional features.

## Getting started
At first you need to ensure that you have all system requirements correctly
installed. A guideline is therefore written in the wiki on
https://gitlab.com/vqeg/streamsim/wikis/system-requirements

Before you run the chain the first time it is recommended to setup a further
folder where you want to store all files generated by the chain. Therefore the
chain delivers a useful setup-tool, which sets up the complete required folder
and configuration file structure, using the following command:

```bash
python chain.py setup -p <PATH_TO_SETUP>
```

Please note, that you need to replace the keyword ```<PATH_TO_SETUP>``` with the
actual path where you want to set up the chain in. Further information about
this step is also given in the wiki under the following URL:
https://gitlab.com/vqeg/streamsim/wikis/setup

After the folder and configuration structure has been onetime setup, the
chain's configuration has to be done. Therefore some further information are
given in the appropriate configuration file headers and obviously in the wiki:
https://gitlab.com/vqeg/streamsim/wikis/setup

## How to use

In short the tool chain can be executed by the command:

```bash
python chain.py -p <EXECUTION_PATH>
```

This command will execute the complete processing chain from the encoding step
until the final decoding step. But it is also possible to call each step
individually or to execute all steps until/from a specific state. More details
about that are given here:
https://gitlab.com/vqeg/streamsim/wikis/usage

## Further material

* Advanced usage: https://gitlab.com/vqeg/streamsim/wikis/home#advanced-usage
* Developers guide: https://gitlab.com/vqeg/streamsim/wikis/home#developers-guideline
* Example results: https://gitlab.com/vqeg/streamsim/wikis/sample-results