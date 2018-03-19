System dependencies:

 * **qemu**: to spin-up the VM.
 * **qemu-img**: to create the disk snapshot.
 * **genisoimage**: to generate the cloudinit cdrom.

Install system dependencies with::

    $ sudo dnf install qemu qemu-img genisoimage

Clone::

    $ git clone https://github.com/apahim/avocado_qemu.git
    $ cd avocado_qemu

Package dependencies:

 * **avocado-framework**: the base framework avocado_qemu inherits from.
 * **aexpect**: lib for interaction with the VM console.

Package dependencies are satisfied by `setup.py`.

Install package with::

    $ pip install .

