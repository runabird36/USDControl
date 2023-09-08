
from pxr import Gf
import collections
nodes = ['|magicianAcrwd_rig|jnt|Root_M',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_L',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_L|HipPart1_L',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_L|HipPart1_L|HipPart2_L',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_L|HipPart1_L|HipPart2_L|Knee_L',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_L|HipPart1_L|HipPart2_L|Knee_L|KneePart1_L',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_L|HipPart1_L|HipPart2_L|Knee_L|KneePart1_L|KneePart2_L',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_L|HipPart1_L|HipPart2_L|Knee_L|KneePart1_L|KneePart2_L|Ankle_L',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_L|HipPart1_L|HipPart2_L|Knee_L|KneePart1_L|KneePart2_L|Ankle_L|Toes_L',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_L|HipPart1_L|HipPart2_L|Knee_L|KneePart1_L|KneePart2_L|Ankle_L|Toes_L|ToesEnd_L',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_R',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_R|HipPart1_R',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_R|HipPart1_R|HipPart2_R',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_R|HipPart1_R|HipPart2_R|Knee_R',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_R|HipPart1_R|HipPart2_R|Knee_R|KneePart1_R',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_R|HipPart1_R|HipPart2_R|Knee_R|KneePart1_R|KneePart2_R',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_R|HipPart1_R|HipPart2_R|Knee_R|KneePart1_R|KneePart2_R|Ankle_R',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_R|HipPart1_R|HipPart2_R|Knee_R|KneePart1_R|KneePart2_R|Ankle_R|Toes_R',
 '|magicianAcrwd_rig|jnt|Root_M|Hip_R|HipPart1_R|HipPart2_R|Knee_R|KneePart1_R|KneePart2_R|Ankle_R|Toes_R|ToesEnd_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M|NeckPart1_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M|NeckPart1_M|Head_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M|NeckPart1_M|Head_M|Eye_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M|NeckPart1_M|Head_M|Eye_L|EyeEnd_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M|NeckPart1_M|Head_M|Eye_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M|NeckPart1_M|Head_M|Eye_R|EyeEnd_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M|NeckPart1_M|Head_M|HeadEnd_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M|NeckPart1_M|Head_M|Jaw_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Neck_M|NeckPart1_M|Head_M|Jaw_M|JawEnd_M',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Cup_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Cup_L|PinkyFinger1_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Cup_L|PinkyFinger1_L|PinkyFinger2_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Cup_L|PinkyFinger1_L|PinkyFinger2_L|PinkyFinger3_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Cup_L|PinkyFinger1_L|PinkyFinger2_L|PinkyFinger3_L|PinkyFinger4_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Cup_L|RingFinger1_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Cup_L|RingFinger1_L|RingFinger2_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Cup_L|RingFinger1_L|RingFinger2_L|RingFinger3_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Cup_L|RingFinger1_L|RingFinger2_L|RingFinger3_L|RingFinger4_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|IndexFinger1_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|IndexFinger1_L|IndexFinger2_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|IndexFinger1_L|IndexFinger2_L|IndexFinger3_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|IndexFinger1_L|IndexFinger2_L|IndexFinger3_L|IndexFinger4_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|MiddleFinger1_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|MiddleFinger1_L|MiddleFinger2_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|MiddleFinger1_L|MiddleFinger2_L|MiddleFinger3_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|MiddleFinger1_L|MiddleFinger2_L|MiddleFinger3_L|MiddleFinger4_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|ThumbFinger1_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|ThumbFinger1_L|ThumbFinger2_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|ThumbFinger1_L|ThumbFinger2_L|ThumbFinger3_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|ThumbFinger1_L|ThumbFinger2_L|ThumbFinger3_L|ThumbFinger4_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_L|Shoulder_L|ShoulderPart1_L|ShoulderPart2_L|Elbow_L|ElbowPart1_L|ElbowPart2_L|Wrist_L|Weapon_L',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Cup_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Cup_R|PinkyFinger1_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Cup_R|PinkyFinger1_R|PinkyFinger2_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Cup_R|PinkyFinger1_R|PinkyFinger2_R|PinkyFinger3_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Cup_R|PinkyFinger1_R|PinkyFinger2_R|PinkyFinger3_R|PinkyFinger4_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Cup_R|RingFinger1_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Cup_R|RingFinger1_R|RingFinger2_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Cup_R|RingFinger1_R|RingFinger2_R|RingFinger3_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Cup_R|RingFinger1_R|RingFinger2_R|RingFinger3_R|RingFinger4_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|IndexFinger1_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|IndexFinger1_R|IndexFinger2_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|IndexFinger1_R|IndexFinger2_R|IndexFinger3_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|IndexFinger1_R|IndexFinger2_R|IndexFinger3_R|IndexFinger4_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|MiddleFinger1_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|MiddleFinger1_R|MiddleFinger2_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|MiddleFinger1_R|MiddleFinger2_R|MiddleFinger3_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|MiddleFinger1_R|MiddleFinger2_R|MiddleFinger3_R|MiddleFinger4_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|ThumbFinger1_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|ThumbFinger1_R|ThumbFinger2_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|ThumbFinger1_R|ThumbFinger2_R|ThumbFinger3_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|ThumbFinger1_R|ThumbFinger2_R|ThumbFinger3_R|ThumbFinger4_R',
 '|magicianAcrwd_rig|jnt|Root_M|Spine1_M|Spine1Part1_M|Spine2_M|Spine2Part1_M|Chest_M|Scapula_R|Shoulder_R|ShoulderPart1_R|ShoulderPart2_R|Elbow_R|ElbowPart1_R|ElbowPart2_R|Wrist_R|Weapon_R']

times = (1,30)

class UndoChunk(object):
    """A Python context that undoes any Maya command that is run inside of it.

    with UndoChunk():
        cmds.polySphere()  # This will get undone, later.

    """

    def __enter__(self):
        """Start recording commands to undo."""
        cmds.undoInfo(openChunk=True)

        return self

    def __exit__(self, exec_type, exec_value, traceback):
        """Undo any commands that were done while this context was left open."""
        needs_undo = not cmds.undoInfo(undoQueueEmpty=True, q=True)
        cmds.undoInfo(closeChunk=True)

        if needs_undo:
            # Only undo if there are any commands to undo. If you try
            # to run undo when there's nothing that can be undone, Maya
            # will raise a RuntimeError.
            #
            cmds.undo()
            
def get_node_transforms_at_times(nodes, times, space):
    """Get the transform matrices of every node at the given times.

    Args:
        nodes (iter[str]):
            The Maya nodes to get transformation data from.
        times (iter[float or int]):
            The values that will be queried for each node-transform.
        space (str):
            The possible transformations that can be queried.
            Options: ["local", "world"].

    Raises:
        ValueError: If the given `space` is not "local" or "world".

    Returns:
        list[list[`pxr.Gf.Matrix4d`]]:
            The transforms for each node in `nodes` for each time in `times`.
            In other words, the list is stored like this
            - node1
                - time1 transform
                - time2 transform
                - time3 transform
            - node2
                - time1 transform
                - time2 transform
                - time3 transform

    """
    spaces = {"local": ".matrix", "world": ".worldMatrix"}

    try:
        attribute_name = spaces[space]
    except KeyError:
        raise ValueError(
            'Space "{space}" is invalid. Options were, "{spaces}".'.format(
                space=space, spaces=sorted(spaces)
            )
        )

    transforms = []

    with UndoChunk():
        matrix_node = cmds.createNode("multMatrix")
        matrix_input = matrix_node + ".matrixIn[0]"

        for node in nodes:
            cmds.connectAttr(node + attribute_name, matrix_input, force=True)
            time_transforms = []

            for time_code in times:
                time_transforms.append(
                    Gf.Matrix4d(*cmds.getAttr(matrix_input, time=time_code))
                )

            transforms.append(time_transforms)

    return transforms
    
    
def get_node_transforms_at_time(nodes, time_code, space):
    """Get the transform matrices of every node at the given times.

    Args:
        nodes (iter[str]):
            The Maya nodes to get transformation data from.
        time_code (float or int):
            The value that will be queried for each node.
        space (str):
            The possible transformations that can be queried.
            Options: ["local", "world"].

    Raises:
        ValueError: If the given `space` is not "local" or "world".

    Returns:
        list[`pxr.Gf.Matrix4d`]:
            The transform of each node in `nodes` for the given time.

    """
    transforms_per_time = get_node_transforms_at_times(nodes, [time_code], space)

    return [transform[0] for transform in transforms_per_time]



STEP = 1.0


def frange(start, stop=None, step=STEP):
    """Create a range of values like Python's built-in "range" function.

    This function will include `start` in its return results but
    excludes `stop`. Just like the way that Python's built-in "range"
    function does.

    Reference:
        https://pynative.com/python-range-for-float-numbers/

    Args:
        start (float or int):
            The value that will start the range.
        stop (float or int or NoneType, optional):
            The value that is used to stop iterating. If no value is
            given then this range will start at 0 and go until it
            reaches the `start` value.
        step (float or int, optional):
            The rate that `start` advances to `stop`. Default: 1.0.

    Yields:
        float or int: The start range + every value

    """
    # Use float number in range() function
    # if stop and step argument is null set start=0.0 and step = 1.0
    if stop is None:
        stop = start
        start = 0.0

    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break

        yield start

        start += step




def get_joint_world_space_transforms(joints, times):
    """Get the world-space matrices for every given joint at every given time.

    Args:
        joints (list[str]):
            The paths to every Maya node to get world-space matrices for.
        times (iter[float or int]):
            The time code values that will be used to query the
            transforms for each joint in `joints`.

    Returns:
        dict[int or float, list[int]]:
            The matrices for every joint in `joints` for each time in
            `times`. The return values is a **flat** matrix. (It's not a
            4x4 matrix, it's a list of 16 elements.)

    """
    output = collections.defaultdict(list)

    for node_time_transforms in get_node_transforms_at_times(joints, times, "world"):
        for time_code, time_transform in zip(times, node_time_transforms):
            output[time_code].append(time_transform)

    return dict(output)

def _setup_rest_transforms(nodes, time_code):
    """Describe the position for every joint in a Skeleton when it is not animated.

    The UsdSkel documentation states that animation can be authored
    sparsely. If a joint has no transform information, it falls back to
    the transform that's authored on its restTransforms Property.

    That means that every transform in restTransform must be in
    local-space, because joint animations are also in local-space (they
    have to match in order to be a valid fallback value).

    Important:
        The order of `nodes` has to match the order of the joints
        Property that is authored on `skeleton`. (You can author the
        Property before or have running this function, as long as it's
        the same).

    Args:
        nodes (list[str]):
            The Maya joints that will be used to get local-space rest
            transforms.
        skeleton (`pxr.UsdSkel.Skeleton`):
            The USD skeleton that the new restTransforms Property will
            be applied onto.
        time_code (float or int):
            The time which is used to sample the transform for each node
            in `nodes`.

    """
    transforms = get_node_transforms_at_time(nodes, time_code, "local")
    pprint(transforms)
    #attribute = skeleton.CreateRestTransformsAttr(transforms)
    #attribute.SetMetadata(
    #    "comment", "Every value in this attribute is a local-space transform."
    #)



start = times[0]
end   = times[1]
time_codes = list(frange(start, end))
   
transforms = get_node_transforms_at_time(nodes, start, "world")



joint_world_space_transforms = get_joint_world_space_transforms(nodes, time_codes)

transforms_local = _setup_rest_transforms(nodes, start)



