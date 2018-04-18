#ifndef PDUR_H
#define PDUR_H

#define PDUR_VENDOR_ID		   VENDOR_ID_MENTOR_GRAPHICS
#define PDUR_MODULE_ID		   5 /* Update */
#define PDUR_AR_MAJOR_VERSION  3
#define PDUR_AR_MINOR_VERSION  1
#define PDUR_AR_PATCH_VERSION  5
#define PDUR_SW_MAJOR_VERSION  2
#define PDUR_SW_MINOR_VERSION  0
#define PDUR_SW_PATCH_VERSION  0



/* ERROR CODES */
#define PDUR_E_CONFIG_PTR_INVALID 		0x06
#define PDUR_E_INVALID_REQUEST 			0x01
#define PDUR_E_PDU_ID_INVALID			0x02
#define PDUR_E_TP_TX_REQ_REJECTED		0x03
#define PDUR_E_DATA_PTR_INVALID			0x05
#define PDUR_E_BUFFER_ERROR				0x06
#define PDUR_E_INIT_FAILED				0x0X /* Check error code */

#include "PduR_Cfg.h"
#include "PduR_Types.h"
#include "../CanIf/CanIf_Types.h"


extern const PduR_PBConfigType *PduRConfig;

/*  The state of the PDU router. */
extern PduR_StateType PduRState;


/* General PDU Router functionality */
void PduR_Init(const PduR_PBConfigType* ConfigPtr); /* SID: 0x00 */
void PduR_GetVersionInfo(Std_VersionInfoType* versionInfo); /* SID: 0x17 */
uint32 PduR_GetConfigurationId(void); /* SID: 0x18 */


/* CAN Interface functions */
void PduR_CanIfRxIndication(PduIdType CanRxPduId, const uint8* CanSduPtr); /* SID: 0x01 */
void PduR_CanIfTxConfirmation(PduIdType CanTxPduId); /* SID: 0x02 */
void PduR_CanTpRxIndication(PduIdType CanTpRxPduId, NotifResultType Result); /* SID: 0x04 */

/* COM */
Std_ReturnType PduR_ComTransmit(PduIdType ComTxPduId, const PduInfoType *PduInfoPtr); /* SID: 0x15 */

/*		PduR structs		*/
typedef struct PduRBswModule PduRBswModule;
typedef struct Pdu Pdu;

struct PduRBswModule{
	PduRBswModule* PduRBswModuleRef;
	boolean PduRRetransmission;
	boolean PduRUseTag;
	boolean PduRTxConfirmation;
	boolean PduRCancelTransmit;
	boolean PduRCommunicationInterface;
	boolean PduRTransportProtocol;
	boolean PduRTriggertransmit;
	boolean PduRUpperModule;
	boolean PduRLowerModule;
	boolean PduRChangeParameterApi;
	boolean PduRCancelReceive;
}PduRBswModules;

typedef struct {
	boolean PduRDevErrorDetect;
	boolean PduRVersionInfoApi;
	boolean PduRZeroCostOperation;
	boolean PduRMetaDataSupport;
} PduRGeneral;

typedef enum{
	PDUR_DIRECT,
	PDUR_TRIGGERTRANSMIT
} PduRDestPduDataProvision;

typedef struct {
	uint16 PduRSourcePduHandleId;
	boolean PduRSrcPduUpTxConf;
	Pdu* PduRSrcPduRef;
} PduRSrcPdu;

typedef struct {
	uint8 PduRDefaultValueElement;
	uint32 PduRDefaultValueElementBytePosition;
} PduRDefaultValueElement;

typedef struct {
    PduRDefaultValueElement* PduRDefaultValueElement;
} PduRDefaultValue;

typedef struct {
	uint32 PduRTpBufferLength;
} PduRTpBuffer;

typedef struct {
    uint16 PduRMaxTpBufferNumber;
    PduRTpBuffer* PduRTpBuffer;
} PduRTpBufferTable;

typedef struct {
	uint32 PduRPduMaxLength;
	uint8 PduRTxBufferDepth;
} PduRTxBuffer;

typedef struct {
    uint16 PduRMaxTxBufferNumber;
    PduRTxBuffer* PduRTxBuffer;
} PduRTxBufferTable;

typedef struct {
    PduRDestPduDataProvision PduRDestPduDataProvision;
    uint16 PduRDestPduHandleId;
    uint16 PduRTpThreshold;
    boolean PduRTransmissionConfirmation;
    Pdu* PduRDestPduRef;
    PduRTxBuffer* PduRDestTxBufferRef;
    PduRDefaultValue PduRDefaultValue;
} PduRDestPdu;


typedef struct {
	boolean PduRIsEnabledAtInit;
	uint16 PduRRoutingPathGroupId;
	PduRDestPdu* PduRDestPduRef;

} PduRRoutingPathGroup;

typedef struct {
	PduRDestPdu* PduRDestPdu;
	PduRSrcPdu PduRSrcPdu;
} PduRRoutingPath;

typedef struct {
	PduRRoutingPath* PduRRoutingPath;
} PduRRoutingTable;

typedef struct {
	uint16 PduRConfigurationId;
	uint16 PduRMaxRoutingPathCnt;
	uint16 PduRMaxRoutingPathGroupCnt;
	uint16 PduRMaxRoutingTableCnt;
	PduRRoutingPathGroup* PduRRoutingPathGroup;
	PduRRoutingTable* PduRRoutingTable;
	PduRTpBufferTable PduRTpBufferTable;
	PduRTxBufferTable PduRTxBufferTable;
} PduRRoutingTables;

struct Pdu {
	ComIPdu_type ComPduIdRef;
	PduRSrcPdu PduRSrcPduRef;
	PduRDestPdu PduRDestPduRef;
	CanIf_RxPduCfgType CanIfRxPduRef;
};

#endif /* PDUR_H */