import rclpy
from rclpy.node import Node
from irobot_create_msgs.msg import AudioNote, AudioNoteVector
from builtin_interfaces.msg import Duration


class BeepNode(Node):
    def __init__(self):
        super().__init__('beep_node')

        self.publisher_ = self.create_publisher(AudioNoteVector, 'cmd_audio', 10)

        self.timer = self.create_timer(2.0, self.publish_beep)

    def publish_beep(self):
        msg = AudioNoteVector()
        msg.append = False

        frequencies = [880, 440, 880, 440]
        for freq in frequencies:
            note = AudioNote()
            note.frequency = freq
            note.max_runtime = Duration(sec=0, nanosec=300_000_000)
            msg.notes.append(note)

        self.publisher_.publish(msg)
        self.get_logger().info('삐뽀삐뽀 시작!')


def main(args=None):
    rclpy.init(args=args)
    node = BeepNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()