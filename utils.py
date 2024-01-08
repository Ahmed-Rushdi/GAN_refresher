import matplotlib.pyplot as plt


def plot_reconstructed_images_and_encodings(original, encodings, reconstructed):
    n = original.shape[0]
    plt.figure(figsize=(20, 4))
    for i in range(n):
        ax = plt.subplot(3, n, i + 1)
        plt.imshow(original[i])
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        if i == 0:
            ax.set_title("Original Images", loc="left", fontsize=20)
        ax = plt.subplot(3, n, i + 1 + n)
        plt.imshow(encodings[i])
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        if i == 0:
            ax.set_title("Encodings", loc="left", fontsize=20)
        ax = plt.subplot(3, n, i + 1 + 2 * n)
        plt.imshow(reconstructed[i])
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        if i == 0:
            ax.set_title("Reconstructed Images", loc="left", fontsize=20)
    plt.show()


def noisify(image, noise_type, noise_factor=0.2):
    implemented_noise = {"static", "b&p"}
    if noise_type not in implemented_noise:
        raise ValueError("results: noise_type must be one of %r." % valid)
    if noise_type == "static":
        noisy_image = image + noise_factor * np.random.normal(
            loc=0.0, scale=1.0, size=image.shape
        )
        return np.clip(noisy_image, 0.0, 1.0)
    elif noise_type == "b&p":
        noisy_image = image.copy()
        rdn = np.random.random(size=image.shape)
        apply_noise = rdn < noise_factor
        noisy_image[apply_noise] = 1 - noisy_image[apply_noise]
        return noisy_image
