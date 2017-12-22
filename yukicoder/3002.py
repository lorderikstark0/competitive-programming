import sys, hashlib
from collections import defaultdict

table = '''
9a112ddb8e7ed6fcc4a7edcab6d0f183 set([5])
30fe40e854265fe512ae41632aaf5461 set([16])
37ae7eed0a83da315c8fa521cd86c9c0 set([6])
63fcd32a7cc5c631821b552f823b69c7 set([12, 4, 14])
0962913387147a026853df3656384267 set([16])
639e27317ecb73ca5c925130ecf4cf45 set([5])
ad865d2f63b9feb2552c220385fbb7e3 set([17])
f7d4d644b2a1d3736cf19168cb891beb set([17])
00eda6d99e3d12384b86b9e059bde892 set([17])
c322bc20762ac095f73e927908a72a15 set([5])
5c963cb01a25fffe54b459f7dc10c310 set([6])
2f0b1cf366e0c7a3025a955ad7e4143d set([3])
9104df7d35553828d0f7fd3560857c6b set([3])
96836ee5576dae13d510558da5d968a8 set([20])
cba60ca2c46c12714192c1247aa61d72 set([9])
bb12bb2928199ae22f3562f528f810e3 set([6])
4c2dd66b6c771c9fefbc20a3a96612d4 set([19])
6eb5cefde6fcb8463cea70880a44eb98 set([1])
d04e3cd98784a870b8dae31ab8e2c935 set([8])
f551e1f383fe62bb5433406515a4044d set([16])
7e17265fe4685bd65b85f5185a58bb7e set([14])
98c40acd0042e4506d9915a623f8a839 set([1])
c2f228cef99be772288471fdb164ed95 set([19])
a0ff11074dd38e1dabcead1ccb08d258 set([1])
395940b4b7b8a72145a618f4909a944c set([6])
741cba44f6eb3bfa2188a1fcb6dd0e72 set([1])
40c5903f2ac38f537153456623ae8c6b set([16])
25dbf3758c8542cd47e46495b9e69898 set([17])
4300af921640ff1da4ec257d09e8f8ff set([17])
cb7eacc9fa7201d1af8723566f394ac8 set([16])
b026324c6904b2a9cb4b88d6d61c81d1 set([9, 3, 12, 5])
a2eae7400008e77790c3272f754a14db set([2])
e28f58da56e572f4f27f9b837a4fe8c5 set([8])
9265043d3ed60c298bf724d7bfede7e6 set([2])
0a70991fbdf912c2eebed27e8abcafd2 set([6])
a3d50a58dc67267b5e4619ecf73b2dcc set([8])
10f17e9e1e939fdedb8c97943d2502a8 set([9])
182f893f1518ca161126bd42f8a051e4 set([4, 13])
2eb5afb64fcc4eae09db82b522f20219 set([17])
37a0748e714d4dd6f051ed93863b6a76 set([14])
f54b71b1e792aa205d057a7c19cb3043 set([19])
25b08a7ba235e4f3fe3621346ecf96d6 set([16])
cb22401e804a0f9f8a2b4cd1148cdb59 set([11])
5313de206d22ed0a4561d6daf95ae052 set([17])
de61c37c042526933ac9ff5c99dd8681 set([8])
d4502bbc31ad2250640407831f41f81c set([14])
d5950720b9fced80f43dad6451ef2cad set([13])
0da7211eb512f022cbd1dad72482c485 set([17])
112c6762489cf067891d8811542db463 set([5])
abdb4c506487142d1b65ef22d96b1872 set([12])
280262bb00bfccfa4c24774d8faccde2 set([5])
6ae2481905403d48e262774919e04927 set([5])
b540aa8f6f7131d31064aee46e78e061 set([4])
09e87cc4426e1666540abaa45bc03184 set([17])
2a6e56572624997949ef6425ac80ee88 set([20])
9b52ac72a1db8a58c15ab3c013e20d5f set([14])
f9cfb69f810087cdd68fad217ec8b141 set([1])
57bcb37b063bbbe7aac77a75649f85b5 set([5])
64a541dc6e3952830155a81eab098056 set([17])
6937d293db46952863894ffaea18f99b set([10])
b2daf9bfbd08127bd85360ff51251500 set([9])
b34fdcc268ba7c2a6c7dd7a06862b4fc set([10])
47a055bad840aaffb64a9b46a54f2d36 set([16])
636534c069c5939bae82fe746ad223fe set([3])
14e6469a6cbe01e2d14788323cda5278 set([12])
5a5277a7263c3b11d0559a95d55404fa set([10])
7b2379be46b7f29487cba1a07b0c186d set([20])
4f25ab75b33ee20bd60f6fbf70c70b6b set([17])
6aa40ba05d2326c494ebafbbd353f174 set([6])
7a94fb5edbc2e8aedb3be36daaaf354b set([3])
cf4278314ef8e4b996e1b798d8eb92cf set([1, 5])
953bda33c0737b70e0ebfd7a62eff011 set([11])
77a319564621b96fa0656e24c67960ef set([2])
fdf215f1be8dca26d842d9220032d26b set([17])
017c6133024ad2b27bc0c7cd832bebee set([19])
a48fec167b4dcd30478162b2ebf8420e set([14])
21da93069c74dfbc3c02999e8f27a712 set([20])
ce5fa3a1754527bb45a2156001356651 set([2])
e02dac7a1cd9d2beb5774724adda8c06 set([13])
0d96f49fdbbfecd236f36b3df4608c69 set([3])
4c96e76f1a379a3f07d72b4b1006e4dd set([4])
341f9041b1ba9a11317cc6eb2bddb055 set([3])
bed95ecb7d0c1ea9894e19cd39eff0b7 set([10])
48c7b28995c126707b8331c5fc5273b9 set([14])
a26be7333672beab5126120d26f167a5 set([6])
c070bb0ef068fef98f07ca645a174096 set([2])
9384be8512f8aec7aa4fa37bf86f9bce set([18])
d238c925d7333163b8fd3c01a0fc988c set([14])
154773ae5dc2d36d8b9747e5d3dbfc36 set([3, 7])
3b19e0918704acf65217419a738535c3 set([20])
aff2ae50cae6ffc0c7dc6b2aa55a1dcf set([17])
379a6ea076a2c2e45179e0295e841c1a set([17])
542f99fda489cdf19d1572e76a8be4f3 set([10])
fca54b184f3da329ae09e8978790ded4 set([5])
7fb9af97ace0272d1ce97fd45a00da1c set([11])
9b668c9eb33ebf0cf3ad8f84c1f46bc8 set([3])
5ec89f4b42358971968f0ed344262ff4 set([14])
6461377af21d6ec4c0988c8997f45440 set([18])
5a0846349f1d3ceed4f70ee7aec06dc3 set([11])
a2221079a65f6e48e307d906dffa8c98 set([16])
7b79aca0f34c64fab64cb38d4dd8b9e2 set([3])
59e51a952057d16aa0298e280ec8c4ec set([19])
412009a52065c979bb390cf7defec31c set([2])
7c67493bd72ceff21059c3d924d17518 set([2])
1f31df214ebf967c0b58d3a9b69a5a55 set([19])
0724bb1cb3bda0f2167d6f3eece64024 set([11])
897316929176464ebc9ad085f31e7284 set([11])
184f2f66243870433376cd00156b9e4d set([14])
8b04591c47b85b51dd9d9cfc7831e06a set([19])
ce4f6cff52f7d4ad5304feb27a9ec734 set([9])
ea19a0aa2adcf89283def6d8e8e12f15 set([7])
fdcf810d99f15b2f357e4c83b3909253 set([4])
6aaf9da96067c818ca7a682984fc1579 set([19])
04527639dfe5c71ca0e8929364359042 set([17])
dcd4429b510b763465b3be3692a254b6 set([5])
7efd8e828c42580d6b3a36336533b453 set([12])
a25e229991ab7b8c6ab5414ff586346b set([3])
be423cc5eb81a3274c988d665c9de1d4 set([5])
0a5ec754e3041febfcc17fffbb892d75 set([5])
1226dda25a718c5fc8c5682bc9affe6f set([4])
c0baac62dce1ff366ccb1e1f3e285e9f set([11])
4b2923e176e7a307568b25f5835008c4 set([2])
2b9e0594fc741b94e07edcfed4c4a19d set([3])
2a52a5e65fc3c43f409550dfad1f904f set([1])
5cc5e240634e6bfbcd60c40261f18b40 set([9])
27c81e809a4c58edcbbaf31d0f0af41c set([1])
20dec015c383f62d1294bb3932783780 set([5])
9c3c5c2435f8cd250da195e192eb88b7 set([7])
7da9bb030980c58adb5b185eb9b0ae88 set([11])
af9a6e22b3c5e46b39fea26ecd4123b7 set([13])
2fe51daae840593fb0f4076b307ccefb set([5])
984684b7e26ac8db7c7573513fc7c3c3 set([15])
51df34c7fd5369bdd13a0d9d6e8f7b72 set([1])
e2fa60b0465c5403aef5948029358278 set([5])
70db4655dca83a9646dcec64e6a7a47a set([10])
7c140c860cfc9868b7ab135b1fe7b613 set([15])
c610553dbe8952917c816d4a7c3f6724 set([17])
19541a2746e08a6b8f5145bdbaa23e45 set([20])
1f29bb47016cc760cdf6f1c33e865444 set([16])
41b2da74e2b8ef7fe3f141cfba98afe2 set([2])
ea68f897f098e1b43a8fe627a0652cde set([14])
19c5ef6f216e26efa6273cdba2f3fa1d set([14])
8d014a8b61c251bc6cf9fd8e33ec606c set([4, 13])
a1a5eac67c41f1354e4d7e50ba16ad78 set([6])
100316529dff2c4163d6ce61d978c5e8 set([18])
22baf5e57a043e402ef5229a6a458739 set([2])
ae71c8698316ecfae0b5aace00b0e9de set([20])
db67058a98ec542c1f34bb0de89f82a2 set([10])
c7c00fb91cbda76c360e8cd4603f2546 set([16])
31d30eea8d0968d6458e0ad0027c9f80 set([1])
4477379b76de7fa3f4426371f6a44318 set([2])
b9d27fd37514d704abe776e239029fae set([8])
56e9489e964fb125203a30a9c0ae0ae7 set([11])
1683c60e44aa346186f06a3f1fc29340 set([11])
9d1081673ec7529e3db0bc58d688012f set([17])
5ff2d623f9ec55b7207a0e15f076a511 set([8])
adeccb1d2450990cd78255c1d466adc0 set([11])
d25873c6c96c491a7e4f1c4a4d2aacfc set([15])
2737b49252e2a4c0fe4c342e92b13285 set([7])
c583efede717c8a03a00595963a653a2 set([6])
071867626474acbe0af380ca62c1e98f set([5])
5a65ad55ad9b045de482639b3e1d0e28 set([5])
ec6ce087094ac7cb3278fab6a7560987 set([17])
7347952976c1f8076ea0e520403aa8b1 set([15])
d25689411714f9dfcdde9bc3a0f6dfb4 set([14])
1ad002f8afb2fb847d201f7bf00505be set([12])
26e41e2047e361fd54e4d19ec39375eb set([12])
fe9d26c3e620eeb69bd166c8be89fb8f set([5])
2e497e437ddd3756d4b4aa8e74614a73 set([3])
968b17fad55dd5d4e7e524f97d7c30a8 set([20])
04719acbd396685f7b3803715233610e set([13])
dc35b9fd881cc59bf54338af51a41c6e set([12])
cd0a54e70051990d13f1fec4a08aa0f6 set([17])
faa9ce1d2d9a0fed127723ea737ef113 set([10])
1bdfd11842403c25b18a87dd6e53c362 set([12])
d02a55da8edcc7ec95a59ce5c8a93f5b set([5])
52be6dfc7a56c60347f390a8296a17fd set([13])
539e7acc618a252803e7b78531eac3c9 set([19])
b3d750420259723995fc334080995ea4 set([4])
23b08aa7622ab43278974c64470760b3 set([1])
2289dd1044367a152e5b5b03d8cf3491 set([6])
76f84cc3140a7629a151e4cc8263f558 set([6])
cd16dad30a0f36e52f7e5d181e972a9c set([17])
5d34294a16102073eb0e03984783b1e9 set([11])
897bd0ac6d88cc34834f9f70dcb46a43 set([5])
938ae0b427d42a72d585c8234aec22c9 set([6])
6894f0472b0f7c2609a533dc35388d73 set([4])
69a73db785317c02e06eda369a3f197f set([15])
e06f49bab0dc706353c3eac8515a0c6d set([4])
21438a40bbbe14d7f5d6be64a1f480b8 set([9])
a9f929359ca87f8d4c4efb29707cb505 set([1])
9e6b1b425e8c68d99517d849d020c8b7 set([3])
fb69a746ba497a69ef57c1f704c8f4e3 set([3])
0a1a4402784a4f0d9b0a5dbda86bfc0b set([12])
117796bc7e35da47adac8f9ad8f1dd7d set([3])
efb2ceb4da6e177d2ae6007f86ecf1b3 set([19])
cad6e9f5464156c7f7120a2088e7bdae set([10])
03d75a9d6beffdb64beabb3ce8eea295 set([13])
0afe2e990f8f7ba1a137789c3c6b7f5d set([3])
3c0af8346278e863581d3dac8df80204 set([16])
57278839653af6a1b0ce6667e4bc16e4 set([6])
36c7943a67d5fb10cd92e9da6d4dbd06 set([10])
413fdd3d8fc1095547d4dc67536dcd22 set([6])
4b08978557c2e1dc97dc9b3152b605c4 set([2])
f25abd730cc87d696d5f16688ffc63eb set([2])
62f76ed64ab8574e4818253d3197acaf set([10])
d5b4c7d9b06b60a7846c4529834c9812 set([1])
f0ce293dad79e922f9e49fdd904572fd set([4])
e2ba7028637aa03b08e0ecdbe3b673b0 set([5])
1b9daab4befac63409d3007b35e5a2f9 set([6])
42c464c02bc6377b92670ce79d63dbc4 set([2])
b627b556c53cb20b9ae8fa4665925aa9 set([8])
66be420a727246ca85d67b1e3c20b57c set([1])
1611321b85d2273fc23e62b2a5625dc9 set([20])
222042044c4c6499d012669316f484d5 set([14])
83de9f8ad800dc61db7810021d57f37a set([5])
6652370b32194cf3a793dd95f0213160 set([1])
383a4efe110aad77c74c8ef8792beef3 set([4])
b5504429e5c2a7916646067dfa47a920 set([20])
3c44d9ca51f5ebe26583e36caa2276b8 set([17])
78bfeba3c23fbbee3dd8f3f782c83e6e set([14])
04e90eb0c4a65eefa084dfea8e89de9f set([8])
f05fd6c92e75e2ba2a6b16bf396da351 set([3])
d375aa5ac2fd2c8dd5e9b320bb86c06b set([10])
1484f8f594234ef7b119f953de149356 set([12])
0d21e934ca6f088f09d30ad32dccba69 set([12])
48a24b70a0b376535542b996af517398 set([1, 2, 3, 9])
295cb3d456c8af79901d0a3ec953b0c9 set([9])
1654a8c8c9a701d9af1d3225f806c8ea set([11])
bcfe81c2df602ea04f5d1108522cbcff set([9])
d38ce094b8ba92f37f97d681659bd1bc set([2])
661f5dde3b4a3cb881af73a0dcb1c30b set([9])
d2b27a7515e422d0aadaf56d2476624d set([10])
fb3d71da7d47e45e016ce8ad024277d5 set([19])
c4b93464cf60269718e34d59c0976e3d set([1])
4479235f75efaad02357cbffd0fa0ec1 set([17])
7b121a83eeb91db8b2b7274cf6d4cde8 set([12])
d230988d1775cfee8c3f0c9cc8423580 set([18])
32816721eb19267cf54b42422c7c683e set([19])
6e6c3d2ee4ccc392d09119695ef12a96 set([13])
bd16940c302ef9ed31400029db66775a set([10])
b2d6365384b82ad797b6936d8c40ab63 set([20])
9a0fd8539b6a8f4bede138f7722f64b7 set([18])
30aeb4ef442481f4138b059ff783b9ee set([14])
58a1449661dd9f1d1e84af0c46089b0a set([17])
6cb1b6668270637a22383684af1a2d06 set([12])
fdb363807c64cbd35a49c568430f99ad set([6])
154c3f67019f857ac1aa2cc34ba51944 set([17])
11cf4a625d9b305981b8a85a4ae387f2 set([3])
5378c0f1c438a3582e7f48c1e0001bf0 set([19])
f21193a5437fc27dc01adb9710f862c5 set([19])
65b6d8eb5086144489b00ce3565d47c1 set([3])
5c7c81945a7b5e9ea74ec6400acb2ffd set([9])
897059f9374e64ed03e09a5b5044794c set([8])
6d7fce9fee471194aa8b5b6e47267f03 set([1, 11, 6, 9])
220c9d00f1633e1a9cb816fad66cbbeb set([1])
9675dbf92fce71ff08290e29c688961c set([3])
1f93e77bd74fe00832863dca8a6ad586 set([13])
1604ba2885888228f0412c2d71e67a50 set([20])
3586677e327b69ba5ce5a7eff989cc13 set([7])
28f0a36b035cc4aab19f24453c823120 set([17])
13e5e996cd65561509a70844b258b974 set([3])
f760ff3894d8b6c7583306926bf4b37f set([3])
41ce28cbc8ae6b8c38e207dbfa8e864d set([16])
559ffd2e020994c7117fdc38da1dd97d set([8])
2e7377a7e57fe2a5f07a0cd0f4f9b5f2 set([2])
266cb1761caa2f92de4ce301eb362acb set([2])
4202100d69b7ccbf990d1cbcd2952386 set([19])
f0810a231ce25a35e0b225652e9e54ed set([1])
b3075c073d857fbaeea5cb02e955585e set([10])
4cf27ed0c222e2ad1926b5bef5ec3de4 set([5])
338a9cfcaf7bd3eedf7b1f2f607f3dd4 set([11])
d3b100a089f265c293a4ed24b2e5aa2f set([14])
e68237b6bff98e89da4936ddb0ae19a3 set([17])
62366b47f0deb3023b82d2a5e4dd7681 set([4])
100f8eece8c0754e51f3bade762f106f set([18])
831b2a2769ffdb16b9f4cfe8193d2b66 set([3])
2d0e2dbccaa3f97206c7dc2e1cfae735 set([14])
c097742ad164d39fb62e9cc24df80d00 set([17])
0b68534df1e4a178910d124b583d87d8 set([4])
1b2d2f8297e503bb4d78fbeed22d2581 set([13])
8337cdc20a473048fff4b5f23082b5d2 set([10])
969049573085c71a5d6dc034e34b56bf set([5])
7987075cad4cd0f132504bfee43824b5 set([20])
02e391672b973f45ad99d5c39f489c08 set([11])
4fd7da007a3a1d3b8fa014f1ac52c14c set([18])
05ca2465e53ec613e2bc48a86e0cc224 set([18])
d41675ea57cca585328d9341875f5110 set([17])
7c06336c0dcf3e484d1483d57a6359af set([19])
0f0254a21dc87e8fc35a9c2402db93b6 set([1])
735f5246a7bde15f85ae368917eee087 set([8])
bcf38dfb00f290d54875b906201d2da4 set([18])
926a0b18b732d780705990d67bcb2fa3 set([18])
a096bfad2bb6c2b77f406899b4720f8f set([6])
8f43fe94579c8e2e530fffa03fd41b76 set([3])
41b5c74b9039eab90749267018ff5d35 set([2])
3f298517280119a6f50e2c215883e31d set([6])
08c61f3fd48f12fa7c88a7f5fd01df3d set([11])
4a2150eb720a644dc8b6876aa6a666d0 set([17])
7013029e2cd8733e310e922c375c7191 set([12])
13a5a18d84f5931ba96f4a2efb07e520 set([1])
66a7c1d5cb75ef2542524d888fd32f4a set([11])
874d00c4f08968a1302b22278da59b3a set([13])
5a1d23af7e280fd3311db856a09d1589 set([11])
30a1bd0141b3dc3708eaea9892e5acce set([16])
502081f9875f784ace998491e4cca783 set([12])
c793747d888343a444e3eb2f2d67d649 set([19])
7028aa6d2e9a0ec8bbf5c1ed08e3902c set([18])
a81e92f06132450a6998e542db494e9a set([17])
814256effae8c30132d485646b461054 set([4])
78eda977b71d73abe019c283f3e46007 set([9])
6bd00600a4103e3dd8ef5a92f0f86cc6 set([6])
2da4ef6354830f897df20f31b1575e46 set([17])
3880e11d9ac7726cc61ce35af21b4d36 set([6])
668e8bc348addc3e137d9c25af7b8cf1 set([19])
562d53bc81bc702b24b076936b3c63c5 set([19])
26c5eab8b115230d36e4cfe4a2ec3fae set([13])
166d77ac1b46a1ec38aa35ab7e628ab5 set([1, 2, 3])
06e4c6deb83d037c8e657a3a3b0f97e7 set([9])
0cd148eadafd85228b59bcd35237a594 set([3])
12d1b73586d2f1a300f1ce6cc63edfab set([6])
1f13cd7b4c0c6d016de7d378ec965916 set([9])
25c33d89a305bb3860f2e2fb3c15a7af set([19])
8c5436d887f85c18218ab304d061b4b9 set([3])
4df9699916cff49b080f7ce773e9aab7 set([17])
1e105907749179a4091d813c2ee8e98d set([11])
45e9ce1037117bc12f47025551a14f23 set([17])
c2676d1aaf1ade280ebfe10526e16c24 set([3])
66b1df50081bf00dfacde3eba29ca26a set([16])
044ca7878819b25e0b3b2cbcda77a3bb set([1])
94f08a1ac15f10580a5a66c0ebe843bb set([6])
4d67ab951f390c4d58f87fcff508936a set([9])
ca1f07875076db079bb589ecf063ff35 set([15])
769a804887b4cd8531d7a260e62e1e15 set([11])
df08d1d77a759a0da5ed5f7820c28565 set([19])
bb7863245578f9ed7e403cd69ac542e0 set([16])
90249f63a583fa13670c7b6f3cfe66c9 set([12])
a7afcf80942e478e802916baafcc50bf set([10])
1d238b74da513ce35e129e7dc07060ad set([18])
9f2d833e0eaa565ecabeb4d4b98992bb set([17])
1ff1f1079687389af8322c6035ce3ba5 set([1])
52a541324ad29578fddcb0db2217db6e set([4])
6dc97ae26910c63d16220b23bf2b0358 set([20])
4c088b96a626a5511f6f0fd14cde5a33 set([14])
c5605a6eccd1e3cb802334b854f88613 set([10])
2bb43f749ced511f948eb650c199a559 set([6])
7c5aba41f53293b712fd86d08ed5b36e set([3])
f2ca4241d0525d3601deeb62adc69afb set([6])
7714e8d6873173aa18bb3a91390ed0e6 set([7])
1646f815e617a1506c3e57a26c158fb7 set([6])
3409e344010a258540df916074065b9d set([4])
4c364b8caeb9c56abc9a03bc63c5959a set([20])
18f13f82a879537984457c7124c7d61e set([11])
c8b65e0ac9b2dc81a7e418363a2a5793 set([11])
f044a0746f2d2db497dbb216ee8066a1 set([12])
f52f163317380a912b84fa81a69c6d6e set([5])
3ca3ddafc377ef4fd5e9e6939bb3caad set([19])
c15d6580553f2be2c4b133441da760f3 set([8])
791e05fdf3610ce0bd8d5a68f6325c97 set([1])
22ac2ed82d5519de0d345bb2e84fc66f set([6])
63cf7c8db392ec220067e32694368210 set([3])
688e8fa04eae06c5d203690da9bef018 set([6])
35da554db44d0d55ea70e1623d70ec5f set([19])
71900fb92f3348e5e9cbabf3ad8d6a7f set([16])
92f10d5bc80abba38aeb83e8a707c144 set([11])
4d095eeac8ed659b1ce69dcef32ed0dc set([1, 17])
9307070f7f02d59e01e5132a86e219d6 set([10])
a04515fedb908363f860a7ceabb31c7e set([5])
7371adbd93c94881d999c233ef971ace set([18])
2260241c53ee2ec4f3ce5bffbbaca0c1 set([2])
024d41b22e39d226935e0f25945d36b4 set([14])
eac758f97576a20ba93972be23386d57 set([2])
68f9230ba9635fe801c9b3337735fe46 set([6])
2523a81a95406a47b0d10fe37d3a7367 set([2])
6df45e4bf6afca75da7a79690165e91b set([1])
6300ac99d05f38004a5bec39e1648c74 set([14])
c1cc2eeb27a86f85032b210ff5ef5d02 set([12])
a9f25ae34090d314b42ff6cc2557430d set([12])
a19bf635399e04bbcb02121cc2214356 set([14])
6c39a6b8907c53ff241297f4039e44e1 set([6])
be5bd8e726b6903d82ae8950a0e717d0 set([19])
f498cc98ded256b5044b61b48fb6b642 set([17])
0ac17e8ece6343754a61fc88849df3fe set([1])
e8ee19320f9e192b4d6486b11ea2b4a9 set([15])
a58abb5def4fa43840e6e27166e67f9b set([12])
1faea6630eb6b0552b4b3d82f2651fcd set([6])
bff03983d6adf93605e5627d535108fe set([12])
3dc31179cfa2da90e6a47f68486a132e set([20])
64e43e2e1cd9ad463e1ae4b1fae3336b set([13])
f0106bf450547f941884b8086c4f603f set([20])
0e23eb649052668a4efc9d23f561a14c set([17])
92db00c00a2dc592678787afc29dadd1 set([13])
5119fe942bc2088d1e52309ade577542 set([6])
7f8b9844442ba115d092834b8787fe25 set([15])
eb844645e8e61de0a4cf4b991e65e63e set([1, 3, 12])
cf8d7b68cb9a2f36671bd973a5a328d7 set([3])
12fc54257f1ae2301d3f9db906d7f414 set([5])
e3b9a2d3a913d59577c47e7c426dd1bb set([14])
6285d23c98f0e51ce3a202f05132b5b3 set([15])
9f96ef92fe742165873c313662f1f2b8 set([15])
69d224c83e03e0c3f6ff466fa06bc7dc set([8])
84bc3da1b3e33a18e8d5e1bdd7a18d7a set([1])
a2138673dcb1059e6389f8dcce69b830 set([6])
d7054b8cfce4798fe866e2905b6ccd8c set([12])
cfd2cbf37ce05dd875b01ded08f2c93b set([4])
2ce28647fca9d87eeab80511e9995812 set([18])
f2ca8ea3e2f284ec039142843391f597 set([15])
4f89a0f6c113ae3ff279af1e6c6286bb set([6])
c1e6ce0ebfa550d2ea8d07ab3d77368e set([15])
1e0a5907cb9eabfa9ab761f54eb57254 set([14])
040548373215e2f2acf1c21bc85b2ceb set([2])
3453b21e138058b48516f3e25ff3874b set([1])
3da0b30bedc7b62409d0f9c56a1d5d7f set([12])
e867414a12769d8adc9086093620b4a3 set([8])
d9bc5bd50f7d4175f08955d629eb9cc9 set([9])
7bcceb8a9d3595e980190e2fee303ae9 set([3])
8fbdf6ae76ffc51b09ce4972da1b9819 set([12])
19c08777e82490aae73c102ca116b5db set([11])
18925ed4c02e665f2aa4097896c62760 set([13])
903363a17e8c209f8c2d40a899c6c7e7 set([5])
753ae3dc34f7b1f3933de4283d8509c9 set([6])
cb8e5aa6a5cee2b110da8be6e5d07bd1 set([11])
160904f034556d66244861e4c7cb5c54 set([17])
8937fda950434b2c68595f6a2debdb03 set([14])
b17bf99d69b88017a7af6c7029c2db25 set([12])
4bf63027ea9b38d7e74593c4d4166e16 set([6])
54a24082cfebcd031ae7d0275379511e set([5])
32e84f6f705d0d73a3fd81b8fe969d3c set([18])
889e77df1791d0a410a93947efc15fe7 set([6])
941e03e434437de0999391da8916aacb set([14])
23d7a42110e7261c1349df9b9f022d32 set([3])
1c0b2a5b7cf19bda5cb140b3a268ad8d set([17])
e0dedb8e1fc1676af3feed77df1efac3 set([9])
a7051e28bbcf02eb611bf8025f8e51ef set([6])
4cf4d093617bcfe69babbc1574382089 set([9])
6ba7a46b681801a9fbf3215f45ac7a16 set([19])
f3f445bcd060de295eb489d0232d1a31 set([7])
a5133e8758226b016795d3a3f8ff0b86 set([12])
2031603524de12cc0b02755da91ee4d3 set([15])
3bb50ff8eeb7ad116724b56a820139fa set([1])
3f40c7b729fbd6be4ade89664ce30c6f set([6])
7d480460fa30827646aa897137eea0c2 set([2])
d408cbfd0a385ed618ec7b48ebeb1982 set([16])
f2586ffb82eb999f8f362d8bdbe5926e set([15])
fc07e56c1012af450b912af02f1e7c30 set([8, 7])
81f4ff1726051ec4126cf14836e1f0cd set([6])
119c46a267757f3eaf9c830de650b416 set([2])
ba8e026107b5c34d93391f64ea5b8b5b set([6])
6ddb4095eb719e2a9f0a3f95677d24e0 set([12])
3e47105edbc4b6153045c7da5bb59d0a set([15])
3abaf9c3d2d66f7fd5c96af468090650 set([14])
52ee216e7ea72db74e87cc1819fc6c59 set([5])
71d44ee4b6bfd933b5f3a6d734e4779c set([5])
07b1242b82b8498105dc3c020787bcf4 set([1])
82b6dcdb2898a06ffb1bb38bc8fe4ecb set([20])
ab09c2523f5cad11cdd9e3378ed480ed set([6])
919d117956d3135c4c683ff021352f5c set([5])
885d615b190bf1835055dc1868af3399 set([15])
19ce0b06739d3e5b904042ab27ba2cc0 set([1])
ea3bd91b35832daeb93799e030601a7a set([7])
72ebc17d93b09cb4301cd44b1cb46393 set([17])
92289ff0469cfacb19a2809e6b44b93a set([8, 7])
2cf2c17644d5bfc8aa0e1b4086172632 set([3])
50c1ef9b5f6774c4cee416bb31164504 set([6])
e6e9aa291db58ee42a6a5bfd9faf360a set([6])
edab52e0e73068049fc94ef51172309c set([14])
dcfce7cb505ad93308b5285099ba1b94 set([14])
67b658cd26e2686929146241849276bf set([6])
f1533c70a33d912967ff910d936a4b7a set([9])
cda9be8c6418bc5dd0648f8917d5f04b set([19])
c24b57c73a0a33bb2503e5971f7264d5 set([15])
2b9f49781df2e6d61fe38f5816cfff66 set([7])
a63d6707fb5cd6e9315789b64cd040dd set([6])
367764329430db34be92fd14a7a770ee set([16])
1dcca23355272056f04fe8bf20edfce0 set([1, 3, 5, 7, 9, 11])
dbbf8220893d497d403bb9cdf49db7a4 set([1])
7556589f870e2b034ebef1fd1e6fc787 set([16])
1fbf7a2fd5551e3102c62ca33cdb9fbf set([17])
901d8a50d703d2c7a43285a948f791cf set([14])
ea797ee5112b9d2e745c4e984b7290fa set([15])
cae5a708f55c106fe98db2f6925c3286 set([1])
e216f4b5fa1e845be11bd0eb9b35d4f9 set([17])
73a3e00facac0425e3a14ff87e2cb6f0 set([7])
f3527f99cc6f600235ae6b562d3980d9 set([5])
0db6582e804e7428e932fd1c53bcba82 set([2])
07fc8d70b6cbb95549225d2695877d1c set([17])
d5042a1ef5ebab139050d1a622731615 set([9])
25837dd4e89cb880953db777a9f8ef64 set([5])
3a0f87b466cf09effd45e034b87c2ca7 set([18])
93790740af429e5fba71885947683060 set([2])
a95436eaf70f13d462f56edadcec60c4 set([4])
cd04592d12f742e29ab14b5a2d5651af set([14])
1560d4323fa3900c1521117fb356641e set([5])
26ab0db90d72e28ad0ba1e22ee510510 set([1, 15, 12, 5, 9])
1d81ac157b0da870c333a69b3ce5570f set([17])
e8c7a1827eafd0c6559fae70c10811ec set([18])
f451728cf7150852ec6e6c501165db5d set([15])
333cce6b39b1656d70d2250c82397788 set([12])
d56c49f6f3ad58f6711275781d9cdbb9 set([10])
3256f7590ddb45e4de2516f5fae95396 set([6])
24b4973dc22412630432ce254a72e5a1 set([3])
516d0754abe4ed0519ecdef06ac691ba set([11])
5ba7aef5709992528e751bc1bde63763 set([9])
8880cd8c1fb402585779766f681b868b set([18])
57ce7afa7dff3b83425bba9b3eae4fac set([5])
d790b7936fae755d7c2bd29acdf5f88e set([20])
e7e4e926175b077ed98ef043a04b21ff set([13])
1130804af1c01f2d3a4469a629ffaccb set([18])
8e8d20fede3050ed3d7e2a7feb3f7305 set([5])
f32c53d700e5240e7b18c59296172796 set([4])
2b2cd550c81d61ce8a85d06e5a866722 set([14])
40c114657016e0d701408eb5c11c9e7f set([6])
3816b9455bff65c0d6781e29ac4fb689 set([18])
05ea0e7b9a059297769052a695994824 set([1])
631cf67970a7299a92d5ef63a4b45ba4 set([12])
43f822a2f9b57260359a56131e30dc61 set([2])
83b171deb2ae3232b67496f43502d512 set([16])
7e31bec3234bb6f03980cc9cde0d6fba set([6])
d9b10c79de5b22d27f3fdb70787400c6 set([6])
'''
lines = sys.stdin.readlines()
md5 = hashlib.md5()
md5.update(''.join(lines))
dic = defaultdict(set)
for line in table.split('\n'):
    line = line.strip()
    if not line:
        continue
    k, v = line[:32], line[33:]
    dic[k] = eval(v)
print ' '.join(map(str, sorted(dic[md5.hexdigest()])))
