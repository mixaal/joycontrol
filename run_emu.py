#!/usr/bin/env python3

import threading
import argparse
import asyncio
import logging
import os

from flask import Flask, request
from flask_restful import Resource, Api

from queue import Queue

from aioconsole import ainput

from joycontrol import logging_default as log, utils
from joycontrol.command_line_interface import ControllerCLI
from joycontrol.controller import Controller
from joycontrol.controller_state import ControllerState, button_push, button_press, button_release
from joycontrol.memory import FlashMemory
from joycontrol.protocol import controller_protocol_factory
from joycontrol.server import create_hid_server

logger = logging.getLogger(__name__)


loop = asyncio.get_event_loop()
queue = Queue()

class JoyConRestfull(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(PressA, '/press/a')
        self.api.add_resource(PressB, '/press/b')
        self.api.add_resource(PressX, '/press/x')
        self.api.add_resource(PressY, '/press/y')
        self.api.add_resource(PressUp, '/press/up')
        self.api.add_resource(PressDown, '/press/down')
        self.api.add_resource(PressLeft, '/press/left')
        self.api.add_resource(PressRight, '/press/right')
        self.api.add_resource(PressR, '/press/r')
        self.api.add_resource(PressZR, '/press/zr')
        self.api.add_resource(PressL, '/press/l')
        self.api.add_resource(PressZL, '/press/zl')
        self.api.add_resource(PressHome, '/press/home')
        self.api.add_resource(PressCapture, '/press/capture')
        self.api.add_resource(PressMinus, '/press/minus')
        self.api.add_resource(PressPlus, '/press/plus')

        self.api.add_resource(HoldA, '/hold/a')
        self.api.add_resource(HoldB, '/hold/b')
        self.api.add_resource(HoldX, '/hold/x')
        self.api.add_resource(HoldY, '/hold/y')
        self.api.add_resource(HoldUp, '/hold/up')
        self.api.add_resource(HoldDown, '/hold/down')
        self.api.add_resource(HoldLeft, '/hold/left')
        self.api.add_resource(HoldRight, '/hold/right')
        self.api.add_resource(HoldR, '/hold/r')
        self.api.add_resource(HoldZR, '/hold/zr')
        self.api.add_resource(HoldL, '/hold/l')
        self.api.add_resource(HoldZL, '/hold/zl')

        self.api.add_resource(ReleaseA, '/release/a')
        self.api.add_resource(ReleaseB, '/release/b')
        self.api.add_resource(ReleaseX, '/release/x')
        self.api.add_resource(ReleaseY, '/release/y')
        self.api.add_resource(ReleaseUp, '/release/up')
        self.api.add_resource(ReleaseDown, '/release/down')
        self.api.add_resource(ReleaseLeft, '/release/left')
        self.api.add_resource(ReleaseRight, '/release/right')
        self.api.add_resource(ReleaseR, '/release/r')
        self.api.add_resource(ReleaseZR, '/release/zr')
        self.api.add_resource(ReleaseL, '/release/l')
        self.api.add_resource(ReleaseZL, '/release/zl')


        self.api.add_resource(RStickRight, '/stick/r/right')
        self.api.add_resource(RStickLeft, '/stick/r/left')
        self.api.add_resource(RStickDown, '/stick/r/down')
        self.api.add_resource(RStickUp, '/stick/r/up')
        self.api.add_resource(RStickCenter, '/stick/r/center')


        self.api.add_resource(LStickRight, '/stick/l/right')
        self.api.add_resource(LStickLeft, '/stick/l/left')
        self.api.add_resource(LStickDown, '/stick/l/down')
        self.api.add_resource(LStickUp, '/stick/l/up')
        self.api.add_resource(LStickCenter, '/stick/l/center')
        self.api.add_resource(LStickHValue, '/stick/l/h')
        self.api.add_resource(LStickVValue, '/stick/l/v')

    def run(self):
        self.app.run()


class RStickRight(Resource):
    def post(self):
        queue.put('stick r right')

class RStickLeft(Resource):
    def post(self):
        queue.put('stick r left')

class RStickUp(Resource):
    def post(self):
        queue.put('stick r up')

class RStickDown(Resource):
    def post(self):
        queue.put('stick r down')

class RStickCenter(Resource):
    def post(self):
        queue.put('stick r center')

class LStickRight(Resource):
    def post(self):
        queue.put('stick l right')

class LStickLeft(Resource):
    def post(self):
        queue.put('stick l left')

class LStickUp(Resource):
    def post(self):
        queue.put('stick l up')

class LStickDown(Resource):
    def post(self):
        queue.put('stick l down')

class LStickCenter(Resource):
    def post(self):
        queue.put('stick l center')

class LStickHValue(Resource):
    def post(self):
        v = request.args.get('value')
        if v is not None:
            #print("LStick Horiz Value:"+v)
            queue.put('lvalue h '+v)

class LStickVValue(Resource):
    def post(self):
        v = request.args.get('value')
        if v is not None:
            #print("LStick Vert Value:"+v)
            queue.put('lvalue v '+v)

class ReleaseR(Resource):
    def post(self):
        queue.put('press r')

class ReleaseL(Resource):
    def post(self):
        queue.put('release l')

class ReleaseZR(Resource):
    def post(self):
        queue.put('release zr')

class ReleaseZL(Resource):
    def post(self):
        queue.put('release zl')


class ReleaseA(Resource):
    def post(self):
        queue.put('release a')


class ReleaseB(Resource):
    def post(self):
        queue.put('release b')


class ReleaseX(Resource):
    def post(self):
        queue.put('release x')


class ReleaseY(Resource):
    def post(self):
        queue.put('release y')


class ReleaseLeft(Resource):
    def post(self):
        queue.put('release left')


class ReleaseRight(Resource):
    def post(self):
        queue.put('release right')


class ReleaseUp(Resource):
    def post(self):
        queue.put('release up')


class ReleaseDown(Resource):
    def post(self):
        queue.put('release down')



class HoldR(Resource):
    def post(self):
        queue.put('press r')

class HoldL(Resource):
    def post(self):
        queue.put('hold l')

class HoldZR(Resource):
    def post(self):
        queue.put('hold zr')

class HoldZL(Resource):
    def post(self):
        queue.put('hold zl')


class HoldA(Resource):
    def post(self):
        queue.put('hold a')


class HoldB(Resource):
    def post(self):
        queue.put('hold b')


class HoldX(Resource):
    def post(self):
        queue.put('hold x')


class HoldY(Resource):
    def post(self):
        queue.put('hold y')


class HoldLeft(Resource):
    def post(self):
        queue.put('hold left')


class HoldRight(Resource):
    def post(self):
        queue.put('hold right')


class HoldUp(Resource):
    def post(self):
        queue.put('hold up')


class HoldDown(Resource):
    def post(self):
        queue.put('hold down')

class PressMinus(Resource):
    def post(self):
        queue.put('press minus')


class PressPlus(Resource):
    def post(self):
        queue.put('press plus')

class PressHome(Resource):
    def post(self):
        queue.put('press home')

class PressCapture(Resource):
    def post(self):
        queue.put('press capture')

class PressR(Resource):
    def post(self):
        queue.put('press r')

class PressL(Resource):
    def post(self):
        queue.put('press l')

class PressZR(Resource):
    def post(self):
        queue.put('press zr')

class PressZL(Resource):
    def post(self):
        queue.put('press zl')


class PressA(Resource):
    def post(self):
        queue.put('press a')


class PressB(Resource):
    def post(self):
        queue.put('press b')


class PressX(Resource):
    def post(self):
        queue.put('press x')


class PressY(Resource):
    def post(self):
        queue.put('press y')


class PressLeft(Resource):
    def post(self):
        queue.put('press left')


class PressRight(Resource):
    def post(self):
        queue.put('press right')


class PressUp(Resource):
    def post(self):
        queue.put('press up')


class PressDown(Resource):
    def post(self):
        queue.put('press down')

"""Emulates Switch controller. Opens joycontrol.command_line_interface to send button commands and more.

While running the cli, call "help" for an explanation of available commands.

Usage:
    run_controller_cli.py <controller> [--device_id | -d  <bluetooth_adapter_id>]
                                       [--spi_flash <spi_flash_memory_file>]
                                       [--reconnect_bt_addr | -r <console_bluetooth_address>]
                                       [--log | -l <communication_log_file>]
                                       [--nfc <nfc_data_file>]
    run_controller_cli.py -h | --help

Arguments:
    controller      Choose which controller to emulate. Either "JOYCON_R", "JOYCON_L" or "PRO_CONTROLLER"

Options:
    -d --device_id <bluetooth_adapter_id>   ID of the bluetooth adapter. Integer matching the digit in the hci* notation
                                            (e.g. hci0, hci1, ...) or Bluetooth mac address of the adapter in string
                                            notation (e.g. "FF:FF:FF:FF:FF:FF").
                                            Note: Selection of adapters may not work if the bluez "input" plugin is
                                            enabled.

    --spi_flash <spi_flash_memory_file>     Memory dump of a real Switch controller. Required for joystick emulation.
                                            Allows displaying of JoyCon colors.
                                            Memory dumps can be created using the dump_spi_flash.py script.

    -r --reconnect_bt_addr <console_bluetooth_address>  Previously connected Switch console Bluetooth address in string
                                                        notation (e.g. "FF:FF:FF:FF:FF:FF") for reconnection.
                                                        Does not require the "Change Grip/Order" menu to be opened,

    -l --log <communication_log_file>       Write hid communication (input reports and output reports) to a file.

    --nfc <nfc_data_file>                   Sets the nfc data of the controller to a given nfc dump upon initial
                                            connection.
"""


async def test_controller_buttons(controller_state: ControllerState):
    """
    Example controller script.
    Navigates to the "Test Controller Buttons" menu and presses all buttons.
    """
    if controller_state.get_controller() != Controller.PRO_CONTROLLER:
        raise ValueError('This script only works with the Pro Controller!')

    # waits until controller is fully connected
    await controller_state.connect()

    await ainput(prompt='Make sure the Switch is in the Home menu and press <enter> to continue.')

    """
    # We assume we are in the "Change Grip/Order" menu of the switch
    await button_push(controller_state, 'home')

    # wait for the animation
    await asyncio.sleep(1)
    """

    # Goto settings
    await button_push(controller_state, 'down', sec=1)
    await button_push(controller_state, 'right', sec=2)
    await asyncio.sleep(0.3)
    await button_push(controller_state, 'left')
    await asyncio.sleep(0.3)
    await button_push(controller_state, 'a')
    await asyncio.sleep(0.3)

    # go all the way down
    await button_push(controller_state, 'down', sec=4)
    await asyncio.sleep(0.3)

    # goto "Controllers and Sensors" menu
    for _ in range(2):
        await button_push(controller_state, 'up')
        await asyncio.sleep(0.3)
    await button_push(controller_state, 'right')
    await asyncio.sleep(0.3)

    # go all the way down
    await button_push(controller_state, 'down', sec=3)
    await asyncio.sleep(0.3)

    # goto "Test Input Devices" menu
    await button_push(controller_state, 'up')
    await asyncio.sleep(0.3)
    await button_push(controller_state, 'a')
    await asyncio.sleep(0.3)

    # goto "Test Controller Buttons" menu
    await button_push(controller_state, 'a')
    await asyncio.sleep(0.3)

    # push all buttons except home and capture
    button_list = controller_state.button_state.get_available_buttons()
    if 'capture' in button_list:
        button_list.remove('capture')
    if 'home' in button_list:
        button_list.remove('home')

    user_input = asyncio.ensure_future(
        ainput(prompt='Pressing all buttons... Press <enter> to stop.')
    )

    # push all buttons consecutively until user input
    while not user_input.done():
        for button in button_list:
            await button_push(controller_state, button)
            await asyncio.sleep(0.1)

            if user_input.done():
                break

    # await future to trigger exceptions in case something went wrong
    await user_input

    # go back to home
    await button_push(controller_state, 'home')


def ensure_valid_button(controller_state, *buttons):
    """
    Raise ValueError if any of the given buttons os not part of the controller state.
    :param controller_state:
    :param buttons: Any number of buttons to check (see ButtonState.get_available_buttons)
    """
    for button in buttons:
        if button not in controller_state.button_state.get_available_buttons():
            raise ValueError('Button {button} does not exist on {controller_state.get_controller()}')


async def mash_button(controller_state, button, interval):
    # wait until controller is fully connected
    await controller_state.connect()
    ensure_valid_button(controller_state, button)

    user_input = asyncio.ensure_future(
        ainput(prompt='Pressing the {button} button every {interval} seconds... Press <enter> to stop.')
    )
    # push a button repeatedly until user input
    while not user_input.done():
        await button_push(controller_state, button)
        await asyncio.sleep(float(interval))

    # await future to trigger exceptions in case something went wrong
    await user_input


def _register_commands_with_controller_state(controller_state, cli):
    """
    Commands registered here can use the given controller state.
    The doc string of commands will be printed by the CLI when calling "help"
    :param cli:
    :param controller_state:
    """
    async def test_buttons():
        """
        test_buttons - Navigates to the "Test Controller Buttons" menu and presses all buttons.
        """
        await test_controller_buttons(controller_state)

    cli.add_command(test_buttons.__name__, test_buttons)


    async def stick(*args):
        if not len(args) == 2:
            raise ValueError('"stick" command requires a side and direction as arguments!')

        side, direction = args
        await cli.cmd_stick(side, direction)

    cli.add_command(stick.__name__, stick)

    async def lvalue(*args):
        if not len(args) == 2:
            raise ValueError('"lstick" command requires a direction and value as arguments!')

        direction, value = args
        print('lvalue '+direction+' '+value)
        await cli.cmd_stick('l', direction, value)

    cli.add_command(lvalue.__name__, lvalue)


    # Mash a button command
    async def mash(*args):
        """
        mash - Mash a specified button at a set interval

        Usage:
            mash <button> <interval>
        """
        if not len(args) == 2:
            raise ValueError('"mash_button" command requires a button and interval as arguments!')

        button, interval = args
        await mash_button(controller_state, button, interval)

    cli.add_command(mash.__name__, mash)

    async def press(*args):
        """
        press - Press and release specified buttons

        Usage:
            press <button>

        Example:
            press a b
        """
        if not args:
            raise ValueError('"press" command requires a button!')

        await hold(*args)
        await asyncio.sleep(0.1)
        await release(*args)

    cli.add_command(press.__name__, press)


    # Hold a button command
    async def hold(*args):
        """
        hold - Press and hold specified buttons

        Usage:
            hold <button>

        Example:
            hold a b
        """
        if not args:
            raise ValueError('"hold" command requires a button!')

        ensure_valid_button(controller_state, *args)

        # wait until controller is fully connected
        await controller_state.connect()
        await button_press(controller_state, *args)

    cli.add_command(hold.__name__, hold)

    # Release a button command
    async def release(*args):
        """
        release - Release specified buttons

        Usage:
            release <button>

        Example:
            release a b
        """
        if not args:
            raise ValueError('"release" command requires a button!')

        ensure_valid_button(controller_state, *args)

        # wait until controller is fully connected
        await controller_state.connect()
        await button_release(controller_state, *args)

    cli.add_command(release.__name__, release)

    # Create nfc command
    async def nfc(*args):
        """
        nfc - Sets nfc content

        Usage:
            nfc <file_name>          Set controller state NFC content to file
            nfc remove               Remove NFC content from controller state
        """
        if controller_state.get_controller() == Controller.JOYCON_L:
            raise ValueError('NFC content cannot be set for JOYCON_L')
        elif not args:
            raise ValueError('"nfc" command requires file path to an nfc dump as argument!')
        elif args[0] == 'remove':
            controller_state.set_nfc(None)
            print('Removed nfc content.')
        else:
            _loop = asyncio.get_event_loop()
            with open(args[0], 'rb') as nfc_file:
                content = await _loop.run_in_executor(None, nfc_file.read)
                controller_state.set_nfc(content)

    cli.add_command(nfc.__name__, nfc)


async def _main(args):
    # parse the spi flash
    if args.spi_flash:
        with open(args.spi_flash, 'rb') as spi_flash_file:
            spi_flash = FlashMemory(spi_flash_file.read())
    else:
        # Create memory containing default controller stick calibration
        spi_flash = FlashMemory()

    # Get controller name to emulate from arguments
    controller = Controller.from_arg(args.controller)

    with utils.get_output(path=args.log, default=None) as capture_file:
        # prepare the the emulated controller
        factory = controller_protocol_factory(controller, spi_flash=spi_flash)
        ctl_psm, itr_psm = 17, 19
        transport, protocol = await create_hid_server(factory, reconnect_bt_addr=args.reconnect_bt_addr,
                                                      ctl_psm=ctl_psm,
                                                      itr_psm=itr_psm, capture_file=capture_file,
                                                      device_id=args.device_id)

        controller_state = protocol.get_controller_state()

        joycon_server = JoyConRestfull()

        th = threading.Thread(target=joycon_server.run)
        th.start()

        # Create command line interface and add some extra commands
        cli = ControllerCLI(controller_state, queue)
        _register_commands_with_controller_state(controller_state, cli)
        cli.add_command('amiibo', ControllerCLI.deprecated('Command was removed - use "nfc" instead!'))

        # set default nfc content supplied by argument
        if args.nfc is not None:
            await cli.commands['nfc'](args.nfc)

        #asyncio.ensure_future(cli.run())
        #asyncio.ensure_future(app.run(port='5002'))
        # run the cli
        try:
            await cli.run()
        finally:
            logger.info('Stopping communication...')
            await transport.close()


if __name__ == '__main__':
    # check if root
    if not os.geteuid() == 0:
        raise PermissionError('Script must be run as root!')

    # setup logging
    #log.configure(console_level=logging.ERROR)
    log.configure()

    parser = argparse.ArgumentParser()
    parser.add_argument('controller', help='JOYCON_R, JOYCON_L or PRO_CONTROLLER')
    parser.add_argument('-l', '--log')
    parser.add_argument('-d', '--device_id')
    parser.add_argument('--spi_flash')
    parser.add_argument('-r', '--reconnect_bt_addr', type=str, default=None,
                        help='The Switch console Bluetooth address, for reconnecting as an already paired controller')
    parser.add_argument('--nfc', type=str, default=None)
    args = parser.parse_args()

    loop.run_until_complete(
        _main(args)
    )
