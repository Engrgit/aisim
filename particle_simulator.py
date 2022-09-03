
def compute_particle_time(N, K, *particle_locations):
    latest_particle_time = N - K
    while K !=0:
        # This is assuming we have no rebound
        particle_speed = 1
        distance_covered = 0  # at the beginning
        particle_time = 0  # at the beginning and  particle_speed = distance_covered / particle_time
        left_longest_dist = 0
        right_longest_dist = 0
        particle_list = []
        # if location are the same, reverse direction
        loc = list(particle_locations)
        for i in loc:
            if i > N/2:
                # If particle position is > N/2 --> we move right to N --> we move right
                distance_covered += abs(N - i)  # provided it is moving right
                if distance_covered > right_longest_dist:
                    right_longest_dist = distance_covered
                    distance_covered = 0
            else:
                # If particle position is < N/2 --> we move closer to 0 ---> we move left
                distance_covered = i
                if distance_covered > left_longest_dist:
                    left_longest_dist = distance_covered
                    distance_covered = 0
        K = K-1
    earliest_particle_time = max(left_longest_dist, right_longest_dist)   # particle_speed is constant at 1m/s

    print("Earliest particle time: {}".format(earliest_particle_time))
    print("Latest particle time: {}".format(latest_particle_time))
    particle_time = [earliest_particle_time, latest_particle_time]
    return particle_time


def particle_simulator(N, K, *particle_locations):
    print("Initial locations of particles... %s" % list(particle_locations))
    loc = list(particle_locations)
    # compute earliest_time
    result = compute_particle_time(N, K, *particle_locations)
    print(result)
    return result


def test_simulator():
    assert ((particle_simulator(214, 7, 11, 12, 7, 13, 176, 23, 191)) == [38, 207])
    print("Test Passed")


if __name__ == '__main__':
    test_simulator()