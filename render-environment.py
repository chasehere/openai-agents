import optparse


def parse_args():
  usage = """usage: %prog [options]"""

  parser = optparse.OptionParser(usage)
  help = "The environment to render.  Default is CartPole-v0."
  parser.add_option('--env', help=help, default='CartPole-v0')
  help = "The number of frames to sample from the environment.  Default is 1000"
  parser.add_option('--frames', type='int', help=help, default=1000)
  
  options, args = parser.parse_args()
  
  return options



def render(environment,frames=1000):
  import gym
  env = gym.make(environment)
  env.reset()
  for _ in xrange(frames):
    env.render()
    env.step(env.action_space.sample())



def main():
  options = parse_args()
  render(options.env, options.frames)
 

 
if __name__ == '__main__':
  main()
