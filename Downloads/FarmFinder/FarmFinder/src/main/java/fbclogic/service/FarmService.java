package fbclogic.service;
import java.util.List;

import fbclogic.model.Farm;

public interface FarmService {
    /*
     * saves farm
     * @param farm the farm to save
     */
    Farm saveFarm(Farm farm);
    /*
    * fetches list of farm entities
    * @return list of farms
    */
    List<Farm> fetchFarmList();
    /*
     * updates existing farm
     * @param farm the farm with updated info
     * @param farmID the ID of the farm to update
     */
    Farm updateFarm(Farm farm, Integer farmID);
    /*
     * deletes existing farm
     * @param farmID the ID of the farm to delete
     */
    void deleteFarmByID(Integer farmID);
}
