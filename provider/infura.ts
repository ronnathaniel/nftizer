
import { ethers } from 'ethers';
import * as dotenv from 'dotenv';

dotenv.config()

export const getInfuraProvider = () => {
    const infuraProvider = new ethers.providers.InfuraProvider(
        process.env.ETH_NETWORK,
        process.env.INFURA_PROJECT_ID,

    )

    return infuraProvider
}
