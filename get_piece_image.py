
def get_piece_image(undist, binary_warped, Minv, left_fit, right_fit,path):
    ploty = np.linspace(0, binary_warped.shape[0] - 1, binary_warped.shape[0])
    left_fitx = left_fit[0] * ploty ** 2 + left_fit[1] * ploty + left_fit[2]
    right_fitx = right_fit[0] * ploty ** 2 + right_fit[1] * ploty + right_fit[2]
    print binary_warped.shape
    warp_zero = np.zeros_like(binary_warped).astype(np.uint8)
    color_warp = np.dstack((warp_zero, warp_zero, warp_zero))
    print len(ploty), color_warp.shape
    for n in range(len(ploty)):
        warp_zero[int(ploty[n]), int(left_fitx[n])] = 255
        warp_zero[int(ploty[n]), int(right_fitx[n])] = 255
    newwarp = cv2.warpPerspective(warp_zero, Minv, (undist.shape[1], undist.shape[0]))
    sy = []
    for n in range(len(ploty)):
        color_warp[int(ploty[n]), int(left_fitx[n]), :] = [255, 255, 255]
        color_warp[int(ploty[n]), int(right_fitx[n]), :] = [255, 255, 255]
    color_warp = cv2.warpPerspective(color_warp, Minv, (undist.shape[1], undist.shape[0]))
    for n in range(len(ploty)):
        if sum(newwarp[n,:]) >0:
            sy.append(n)
    # newwarp[sy[0],:] = 255
    # newwarp[sy[len(sy)-1], :] = 255
    # print len(sy), sy[len(sy)-1], sy[0], (sy[len(sy)-1] - sy[0])/41
    color_warp[sy[0], :, :] = [0, 0, 255]
    color_warp[sy[len(sy)-1], :, :] = [0, 0, 255]
    dt = (sy[len(sy)-1] - sy[0])/41
    img_label = 0
    for l in range(dt):

        dx = newwarp[sy[0]+41*l, :].nonzero()

        c = 1
        while len(dx[0]) <= 1:
            dx = newwarp[sy[0] + (41*l) + c, :].nonzero()
            c += 1
        xd = dx[0][len(dx[0])-1] - dx[0][0]
        print xd/41
        color_warp[sy[0] + 41 * l, dx[0][0]:dx[0][len(dx[0])-1]] = [0, 255, 0]
        for h in range((xd/41)+1):
            color_warp[sy[0] + 41 * l:sy[0] + 41 * (l+1), dx[0][0] + h*41] = [255, 0, 0]
            # 保存图片块
            cv2.imwrite(path +  '0000' + '%d' % (img_label) + '.jpg', color_warp[sy[0] + 41*l:sy[0] + 41*(l+1), dx[0][0]+h*41:dx[0][0]+(1+h)*41])
            img_label += 1
    return color_warp
