import argparse
from src.roamers.keyboard_habitat_roamer import KeyboardHabitatRoamer


def main():
    # parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--launch-file-path", default="../visualnav-transformer/deployment/launch/vint_keyboard.launch", type=str)
    parser.add_argument(
        "--hab-env-node-path", default="src/vint_env_launcher.py", type=str
    )
    parser.add_argument(
        "--hab-env-config-path", default="configs/roam_configs/pointnav_rgbd_roam_mp3d_test_scenes.yaml", type=str
    )
    parser.add_argument("--hab-env-node-name", default="roamer_env_node", type=str)
    parser.add_argument("--episode-id", type=str, default="-1")
    parser.add_argument(
        "--scene-id",
        type=str,
        default="data/scene_datasets/mp3d/2t7WUuJeko7/2t7WUuJeko7.glb",
    )
    parser.add_argument(
        "--video-frame-period",
        type=int,
        default=60,
    )
    args = parser.parse_args()

    # start the roamer nodes
    roamer = KeyboardHabitatRoamer(
        launch_file_path=args.launch_file_path,
        hab_env_node_path=args.hab_env_node_path,
        hab_env_config_path=args.hab_env_config_path,
        hab_env_node_name=args.hab_env_node_name,
        video_frame_period=args.video_frame_period,
    )

    # get to the specified episode
    roamer.roam_until_shutdown(args.episode_id, args.scene_id)


if __name__ == "__main__":
    main()
